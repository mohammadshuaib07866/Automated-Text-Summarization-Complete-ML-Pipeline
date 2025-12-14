import os
import sys
from datasets import load_from_disk
from transformers import AutoTokenizer

from textSummarizer.logger.logging import logging
from textSummarizer.entity.entity_config import DataTransformationConfig
from textSummarizer.exceptions.exception import TextSummarizationException


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        try:
            self.config = config
            self.tokenizer = AutoTokenizer.from_pretrained(
                self.config.tokenizer_name
            )
        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def convert_examples_to_features(self, example_batch):
        try:
            inputs = self.tokenizer(
                example_batch["dialogue"],
                max_length=1024,
                truncation=True,
                padding="max_length",
            )

            targets = self.tokenizer(
                example_batch["summary"],
                max_length=128,
                truncation=True,
                padding="max_length",
            )

            return {
                "input_ids": inputs["input_ids"],
                "attention_mask": inputs["attention_mask"],
                "labels": targets["input_ids"],
            }

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def convert(self):
        try:
            logging.info("Starting data transformation")

            dataset = load_from_disk(self.config.data_path)

            tokenized_dataset = dataset.map(
                self.convert_examples_to_features,
                batched=True,
                remove_columns=dataset["train"].column_names,
            )

            save_path = os.path.join(
                self.config.root_dir, "samsum_dataset"
            )
            tokenized_dataset.save_to_disk(save_path)

            logging.info(f"Tokenized dataset saved at: {save_path}")

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())
