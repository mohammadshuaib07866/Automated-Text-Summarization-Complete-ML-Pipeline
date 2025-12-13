import sys
from textSummarizer.logger.logging import logging
from textSummarizer.exceptions.exception import TextSummarizationException


if __name__ == "__main__":
    logging.info("Testing custom exception")

    try:
        raise ValueError("This is a test error")

    except Exception as e:
        raise TextSummarizationException(e, sys)
