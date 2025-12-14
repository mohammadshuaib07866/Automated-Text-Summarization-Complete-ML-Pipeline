import os
import sys
import urllib.request as request
import zipfile
from pathlib import Path

from textSummarizer.logger.logging import logging
from textSummarizer.utils.commons import get_size
from textSummarizer.entity.entity_config import DataIngestionConfig
from textSummarizer.exceptions.exception import TextSummarizationException


class DateIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                logging.info(f"Downloading data from: {self.config.source_URL}")

                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )

                # Defensive check: ensure it's actually a ZIP
                if "text/html" in str(headers):
                    raise ValueError(
                        "Downloaded file is HTML, not a ZIP. "
                        "Please check source_URL (must be raw.githubusercontent.com)"
                    )

                logging.info(f"Downloaded file successfully: {filename}")

            else:
                logging.info(
                    f"File already exists with size: "
                    f"{get_size(Path(self.config.local_data_file))}"
                )

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())

    def extract_zip_file(self):
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)

            logging.info(f"Extracting ZIP file to: {unzip_path}")

            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)

            logging.info("ZIP file extracted successfully")

        except Exception as e:
            raise TextSummarizationException(e, sys.exc_info())
