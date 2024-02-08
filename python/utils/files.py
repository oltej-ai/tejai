import os


def isExist(path: str):
    return path.is_file()


def create_files(files: list):
    for file in files:
        with open(str(file), "w") as f:
            pass
        f.close()


def delete_files(files: list):
    for file in files:
        os.remove(file)
