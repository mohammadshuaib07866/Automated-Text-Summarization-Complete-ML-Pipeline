import os
import sys
import torch

from transformers import (
    TrainingArguments,
    Trainer,
    DataCollatorForSeq2Seq,
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
)

from datasets import load_from_disk

from textSummarizer.logger.logging import logging
from textSummarizer.exceptions.exception import TextSummarizationException
from textSummarizer.entity.entity_config import ModelTrainingConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig):
        try:
            self.config = config
        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def train(self):
        try:
            logging.info("🚀 Model training started")

            device = "cuda" if torch.cuda.is_available() else "cpu"

            tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
            model = AutoModelForSeq2SeqLM.from_pretrained(
                self.config.model_ckpt
            ).to(device)

            data_collator = DataCollatorForSeq2Seq(
                tokenizer=tokenizer, model=model
            )

            logging.info("📦 Loading tokenized dataset")
            dataset = load_from_disk(self.config.data_path)

            training_args = TrainingArguments(
                output_dir=self.config.root_dir,
                num_train_epochs=1,
                warmup_steps=500,
                per_device_train_batch_size=1,
                per_device_eval_batch_size=1,
                gradient_accumulation_steps=16,
                weight_decay=0.01,
                logging_steps=10,
                evaluation_strategy="steps",
                eval_steps=500,
                save_steps=1000000,
                save_total_limit=2,
                fp16=torch.cuda.is_available(),
                report_to="none",
            )

            trainer = Trainer(
                model=model,
                args=training_args,
                tokenizer=tokenizer,
                data_collator=data_collator,
                train_dataset=dataset["train"],
                eval_dataset=dataset["validation"],
            )

            trainer.train()

            logging.info("💾 Saving trained model and tokenizer")

            model.save_pretrained(
                os.path.join(self.config.root_dir, "pegasus-samsum-model")
            )
            tokenizer.save_pretrained(
                os.path.join(self.config.root_dir, "tokenizer")
            )

            logging.info("✅ Model training completed successfully")

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())
