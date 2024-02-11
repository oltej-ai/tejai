def definition(project_type: str = "default") -> dict:
    """
    Defines the recommended structure for a Python project directory, optionally
    customized by project type.

    Args:
        project_type (str, optional): The type of project. Defaults to "default".
            Valid options include:
                - "default": A generic project structure.
                - "web": A project focused on web development.
                - "data-science": A project for data science or machine learning.
                - "api": A project for building APIs.
                - "library": A project for developing reusable Python modules.

    Returns:
        dict: A dictionary containing the recommended files and directories for the
            specified project type.

    Raises:
        ValueError: If the provided project type is invalid.
    """

    default_structure = {
        "default": ["__init__.py"],
        "files": ["README.md", ".gitignore", "config.yaml"],
        "dirs": ["configs", "components", "manifests", "pipelines"],
    }

    project_specific_structures = {
        "web": {
            "dirs": ["static", "templates"],  # Add common web directories
        },
        "data-science": {
            "dirs": [
                "data",
                "notebooks",
                "models",
            ],  # Add data, analysis, and model directories
        },
        "api": {
            "files": ["api_documentation.md"],  # Add API documentation
            "dirs": ["endpoints", "schemas"],  # Add API-specific directories
        },
        "library": {
            "files": ["setup.py", "LICENSE.txt"],  # Add packaging and licensing files
            "dirs": ["tests", "docs"],  # Add testing and documentation directories
        },
    }

    if (
        project_type not in default_structure
        and project_type not in project_specific_structures
    ):
        raise ValueError(f"Invalid project type: {project_type}")

    structure = default_structure.copy()
    if project_type in project_specific_structures:
        structure.update(project_specific_structures[project_type])

    return structure
