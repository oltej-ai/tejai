CONNECTOR_TAG = "kfp"


def component_definition() -> dict:
    return {
        "default": ["__init__.py"],
        "files": ["requirements.txt", "README.md", "Dockerfile", "VERSION", ".dockerignore"],
        "dirs": ["src", "test", "common"],
    }


def manifest_definition() -> dict:
    return {"files": ["component.yaml", "pipeline.json"], "dirs": ["components", "pipelines"]}
