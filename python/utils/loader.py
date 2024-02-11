from typing import Any
import yaml


def load_yaml(path: str) -> Any:
    """
    Loads YAML data from the specified file path.

    Args:
        path (str): The path to the YAML file.

    Returns:
        Any: The parsed YAML data.

    Raises:
        ValueError: If the file is not found.
    """

    try:
        with open(path, "r") as yamlfile:
            data = yaml.safe_load(yamlfile)
        return data
    except FileNotFoundError as e:
        raise ValueError(f"YAML file not found at: {path}") from e
