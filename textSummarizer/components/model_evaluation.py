import os
import sys
import torch
import pandas as pd
from tqdm import tqdm
import evaluate

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk

from textSummarizer.entity.entity_config import ModelEvaluationConfig
from textSummarizer.logger.logging import logging
from textSummarizer.exceptions.exception import TextSummarizationException


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        try:
            self.config = config
        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def generate_batch_sized_chunks(self, elements, batch_size):
        """Split data into batches"""
        for i in range(0, len(elements), batch_size):
            yield elements[i : i + batch_size]

    def calculate_metric_on_test_ds(
        self,
        dataset,
        metric,
        model,
        tokenizer,
        batch_size=8,
        device="cpu",
        column_text="dialogue",
        column_summary="summary",
    ):
        try:
            article_batches = list(
                self.generate_batch_sized_chunks(dataset[column_text], batch_size)
            )
            summary_batches = list(
                self.generate_batch_sized_chunks(dataset[column_summary], batch_size)
            )

            model.eval()

            with torch.no_grad():
                for articles, references in tqdm(
                    zip(article_batches, summary_batches),
                    total=len(article_batches),
                ):
                    inputs = tokenizer(
                        articles,
                        max_length=1024,
                        truncation=True,
                        padding="max_length",
                        return_tensors="pt",
                    ).to(device)

                    summaries = model.generate(
                        input_ids=inputs["input_ids"],
                        attention_mask=inputs["attention_mask"],
                        num_beams=8,
                        max_length=128,
                        length_penalty=0.8,
                    )

                    decoded_preds = [
                        tokenizer.decode(
                            s,
                            skip_special_tokens=True,
                            clean_up_tokenization_spaces=True,
                        )
                        for s in summaries
                    ]

                    metric.add_batch(
                        predictions=decoded_preds,
                        references=references,
                    )

            score = metric.compute()
            return score

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def evaluate(self):
        try:
            logging.info("🚀 Model evaluation started")

            device = "cuda" if torch.cuda.is_available() else "cpu"

            tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
            model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(
                device
            )

            dataset = load_from_disk(self.config.data_path)

            # evaluate only small subset to save time
            test_data = dataset["test"].select(range(10))

            rouge = evaluate.load("rouge")

            scores = self.calculate_metric_on_test_ds(
                dataset=test_data,
                metric=rouge,
                model=model,
                tokenizer=tokenizer,
                batch_size=2,
                device=device,
            )

            rouge_dict = {
                "rouge1": scores["rouge1"],
                "rouge2": scores["rouge2"],
                "rougeL": scores["rougeL"],
                "rougeLsum": scores["rougeLsum"],
            }

            df = pd.DataFrame(rouge_dict, index=["pegasus"])
            df.to_csv(self.config.metric_file_name, index=False)

            logging.info(
                f"✅ Evaluation completed. Metrics saved at {self.config.metric_file_name}"
            )

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())
