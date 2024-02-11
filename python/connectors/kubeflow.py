CONNECTOR_TAG = "kfp"


def component_definition(project_name: str = None) -> dict:
    """
    Defines the recommended structure for a Kubeflow component directory, optionally
    customizing by project name.

    Args:
        project_name (str, optional): The name of the project. If provided, will be
            appended to certain filenames for clearer organization.

    Returns:
        dict: A dictionary containing the recommended component structure.

    Raises:
        ValueError: If the project name contains invalid characters.
    """

    if project_name:
        # Validate project name for allowed characters and length
        # (consider using a regular expression for robustness)
        if not project_name.isalnum() or len(project_name) > 255:
            raise ValueError(
                "Invalid project name. Must be alphanumeric and shorter than 256 characters."
            )

    structure = {
        "default": ["__init__.py"],
        "files": [
            "requirements.txt",
            "README.md",
            f"Dockerfile.{CONNECTOR_TAG}",
            f"VERSION_{project_name}.txt" if project_name else "VERSION.txt",
            ".dockerignore",
        ],
        "dirs": ["src", "test", "common"],
    }

    if project_name:
        # Append project name to directory names for clarity
        structure["dirs"] = [f"{dir}_{project_name}" for dir in structure["dirs"]]

    return structure


def manifest_definition(project_name: str = None) -> dict:
    """
    Defines the recommended structure for a Kubeflow manifest directory, optionally
    customizing by project name.

    Args:
        project_name (str, optional): The name of the project. If provided, will be
            used for naming consistency.

    Returns:
        dict: A dictionary containing the recommended manifest structure.
    """

    structure = {
        "files": [
            "component.yaml",
            f"pipeline_{project_name}.json" if project_name else "pipeline.json",
        ],
        "dirs": ["components", "pipelines"],
    }

    return structure
