import sys
from textSummarizer.logger.logging import logging


class TextSummarizationException(Exception):

    @staticmethod
    def error_message_details(error_message, error_details):
        _, _, exc_tb = error_details

        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        return (
            f"Error occurred in python script [{file_name}] "
            f"at line number [{line_number}] "
            f"with error message [{error_message}]"
        )

    def __init__(self, error_message, error_details):
        super().__init__(error_message)
        self.error_message = self.error_message_details(
            error_message, error_details
        )

    def __str__(self):
        return self.error_message
