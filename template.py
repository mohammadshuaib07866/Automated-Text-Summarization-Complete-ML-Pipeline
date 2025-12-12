import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

project_name: str = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    "config/config.yaml",
    # Research notebooks
    "research/01_data_ingestion.ipynb",
    "research/02_data_validation.ipynb",
    "research/03_data_transformation.ipynb",
    "research/04_model_trainer.ipynb",
    "research/05_model_evaluation.ipynb",
    "research/06_text_summarization.ipynb",
    "research/trials.ipynb",
    # Package scripts
    f"{project_name}/__init__.py",
    f"{project_name}/data_ingestion.py",
    f"{project_name}/data_validation.py",
    f"{project_name}/data_transformation.py",
    f"{project_name}/model_trainer.py",
    f"{project_name}/model_evaluation.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/constants.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/logger/logging.py",
    f"{project_name}/exceptions/__init__.py",
    f"{project_name}/exceptions/exception.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/entity_config.py",
    f"{project_name}/entity/entity_artifact.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/commons.py",
    # Root level files
    "Dockerfile",
    "app.py",
    "main.py",
    "requirements.txt",
    "setup.py",
    "test.py",
    "params.yaml",
]


for files in list_of_files:
    filepath = Path(files)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
