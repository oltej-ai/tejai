import yaml


def load_yaml(path: str):
    with open(path, "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)

    yamlfile.close()
    return data
