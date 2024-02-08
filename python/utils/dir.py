import os


def isExist(path: str):
    return path.is_dir()


def create_dirs(dirs: list):
    for dir in dirs:
        dir.mkdir()


def delete_dirs(dirs: list):
    for dir in dirs:
        os.rmdir(dir)
