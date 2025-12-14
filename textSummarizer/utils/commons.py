import os
import yaml
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from textSummarizer.logger.logging import logging


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file

    Raises:
        ValueError: If YAML file is empty or invalid

    Returns:
        ConfigBox: Parsed YAML content
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)

            if content is None:
                raise ValueError("YAML file is empty")

            logging.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("YAML file structure is invalid")
    except Exception as e:
        raise e


def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Create directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths
        verbose (bool): Whether to log directory creation
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Created directory at: {path}")


def get_size(path: Path) -> str:
    """
    Get file size in KB.

    Args:
        path (Path): Path to the file

    Returns:
        str: File size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
