import os, sys
import logging
from datetime import datetime

# Generate a unique log file name based on the current datatime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_H_%M_%S')}.log"

# Define the path to the log directory
LOG_PATH = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it does'nt exists
os.makedirs(LOG_PATH, exist_ok=True)


# Create the full path for the log file
LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH, mode="a"),
        logging.StreamHandler(sys.stdout),
    ],
)
