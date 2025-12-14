import sys
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DateIngestion
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logger.logging import logging
from textSummarizer.exceptions.exception import TextSummarizationException
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.components.model_evaluation import ModelEvaluation


class TrainingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def get_data_ingestion(self):
        try:
            data_ingestion_config = self.config.get_data_ingestion_config()
            data_ingestion = DateIngestion(config=data_ingestion_config)

            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def get_data_validation(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_files_exists()
        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def get_data_transformation(self):
        try:
            data_transformation_config = self.config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)

            data_transformation.convert()

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def get_model_trainer(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def get_model_evaluation(self):
        try:
            config = ConfigurationManager()
            modle_evaluation_config = config.get_model_evaluation_config()
            model_evaluatin = ModelEvaluation(config=modle_evaluation_config)
            model_evaluatin.evaluate()
        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def run_pipeline(self):
        try:
            logging.info("🚀 Training Pipeline Started")

            self.get_data_ingestion()
            self.get_data_validation()
            self.get_data_transformation()
            self.get_model_trainer()
            self.get_model_evaluation()

            logging.info("✅ Training Pipeline Completed Successfully")

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())
