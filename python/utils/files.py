import os
from pathlib import Path


def is_exist(path: str | Path) -> bool:
    """
    Checks if the given path exists and is a regular file.

    Args:
        path: The path to check. Can be a string or a pathlib.Path object.

    Returns:
        True if the path exists and is a file, False otherwise.

    Raises:
        TypeError: If the path is not a string or a pathlib.Path object.
        FileNotFoundError: If the path does not exist.
    """

    if not isinstance(path, (str, Path)):
        raise TypeError("path must be a string or a pathlib.Path object")

    path = Path(path)  # Ensure Path object for consistent handling

    if not path.exists():
        raise FileNotFoundError(f"Path '{path}' does not exist")

    return path.is_file()


def create_files(files: list, unique_names=False, directory=None, verbose=False):
    """
    Creates empty files based on the provided list of names.

    Args:
        files (list): A list of file names (strings) to create.
        unique_names (bool, optional): If True, generates unique filenames by
            appending an underscore and a running counter (e.g., "file_1.txt").
            Defaults to False.
        directory (str, optional): The directory to create the files in. If
            None, uses the current working directory. Defaults to None.
        verbose (bool, optional): If True, prints messages about each file created.
            Defaults to False.

    Returns:
        list: A list of the created filenames (strings).

    Raises:
        ValueError: If a file already exists with unique_names=False.
        OSError: If there are issues creating the files due to permissions or other errors.
    """

    created_files = []
    counter = 1 if unique_names else 0  # Initialize counter for unique names

    for file in files:
        filename = file
        if unique_names:
            unique_filename = f"{filename}_{counter}"
            filename = unique_filename
            counter += 1

        full_path = os.path.join(directory, filename)

        try:
            with open(full_path, "x") as f:  # Use "x" to create only if nonexistent
                if verbose:
                    print(f"Created file: {full_path}")
                created_files.append(full_path)
        except FileExistsError:
            if unique_names:
                # Continue generating unique names until a non-existent filename is found
                continue
            else:
                raise ValueError(f"File '{full_path}' already exists.")
        except OSError as e:
            raise OSError(f"Error creating file '{full_path}': {e}")

    return created_files


def delete_files(files: list, dry_run=False, log_errors=True):
    """
    Deletes the specified files.

    Args:
        files (list): A list of file paths to delete.
        dry_run (bool, optional): If True, only simulates the deletion and doesn't
            actually remove the files. Defaults to False.
        log_errors (bool, optional): If True, logs any errors encountered during
            deletion. Defaults to True.

    Returns:
        list: A list of successfully deleted files if dry_run is False, otherwise an
            empty list.
    """
    deleted_files = []
    for file in files:
        if os.path.exists(file):
            try:

                if not dry_run:
                    os.remove(file)
                    deleted_files.append(file)
                if not dry_run:
                    print(f"Deleted: {file}")
            except PermissionError as e:
                if log_errors:
                    print(f"Error deleting {file}: {e}")
        else:
            if log_errors:
                print(f"File not found: {file}")

    return deleted_files
