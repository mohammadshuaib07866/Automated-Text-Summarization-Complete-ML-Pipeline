from textSummarizer.constant.constants import *
from textSummarizer.utils.commons import read_yaml, create_directories
from textSummarizer.entity.entity_config import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainingConfig,
    ModelEvaluationConfig,
)
from textSummarizer.exceptions.exception import TextSummarizationException
import sys
from textSummarizer.logger.logging import logging


class ConfigurationManager:
    def __init__(
        self, config_file_path=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH
    ):
        try:
            logging.info("Initializing ConfigurationManager")

            self.config = read_yaml(config_file_path)
            self.params = read_yaml(params_filepath)

            create_directories([self.config.artifacts_root])
            logging.info("Artifacts root directory created")

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            logging.info("Creating Data Ingestion Config")

            config = self.config.data_ingestion
            create_directories([config.root_dir])

            return DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir,
            )

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            logging.info("Creating Data Validation Config")

            config = self.config.data_validation
            create_directories([config.root_dir])

            return DataValidationConfig(
                root_dir=config.root_dir,
                STATUS_FILE=config.STATUS_FILE,
                ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
            )

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            logging.info("Creating Data Transformation Config")

            config = self.config.data_transformation
            create_directories([config.root_dir])

            return DataTransformationConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                tokenizer_name=config.tokenizer_name,
            )

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def get_model_trainer_config(self) -> ModelTrainingConfig:
        try:
            logging.info("Creating Model Trainer Config")

            config = self.config.model_trainer
            params = self.params.TrainingArguments
            create_directories([config.root_dir])

            return ModelTrainingConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                model_ckpt=config.model_ckpt,
                num_train_epochs=params.num_train_epochs,
                warmup_steps=params.warmup_steps,
                per_device_train_batch_size=params.per_device_train_batch_size,
                weight_decay=params.weight_decay,
                logging_steps=params.logging_steps,
                evaluation_strategy=params.evaluation_strategy,
                eval_steps=params.eval_steps,
                save_steps=params.save_steps,
                gradient_accumulation_steps=params.gradient_accumulation_steps,
            )

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        try:
            logging.info("Creating Model Evaluation Config")

            config = self.config.model_evaluation
            create_directories([config.root_dir])

            return ModelEvaluationConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                model_path=config.model_path,
                tokenizer_path=config.tokenizer_path,
                metric_file_name=config.metric_file_name,
            )

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())
