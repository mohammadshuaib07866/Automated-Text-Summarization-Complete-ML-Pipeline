from textSummarizer.pipeline.training_pipeline import TrainingPipeline
from textSummarizer.logger.logging import logging
from textSummarizer.exceptions.exception import TextSummarizationException
import sys


def main():
    try:
        logging.info("========== Text Summarization Pipeline Started ==========")

        pipeline = TrainingPipeline()
        pipeline.run_pipeline()

        logging.info("========== Text Summarization Pipeline Completed ==========")

    except Exception as e:
        logging.error("❌ Pipeline execution failed")
        raise TextSummarizationException(e, sys.exc_info())


if __name__ == "__main__":
    main()
