"""
Utility functions.
"""

import json
import os
import shutil

import joblib

ENCODING = "utf-8"


def silent_remove(fp: str) -> None:
    """
    Removes the given file or dir if it exists.
    Does nothing if not.
    Does not throw any errors,
    """
    try:
        if os.path.isfile(fp):
            os.remove(fp)
        elif os.path.isdir(fp):
            shutil.rmtree(fp)
    except (OSError, FileNotFoundError):
        pass


def silent_rename(src_fp: str, dst_fp: str) -> None:
    """
    Renames the file or directory at src_fp to dst_fp.
    Does nothing if the src_fp does not exist.
    """
    try:
        os.rename(src_fp, dst_fp)
    except FileNotFoundError:
        pass


def get_name(fp: str) -> str:
    """
    Given the filepath, returns the name of the file.
    The name is:
    ```
    <path_to_file>/<name>.<ext>
    ```
    """
    return os.path.splitext(os.path.basename(fp))[0]


def check_files_exist(*args: str):
    """
    args is list of filepaths.
    """
    for dst_fp in args:
        if os.path.exists(dst_fp):
            return True
    return False


def read_json(fp: str) -> dict:
    """
    Reads the json file at the given filepath.
    """
    with open(fp, "r", encoding=ENCODING) as f:
        return json.load(f)


def write_json(fp: str, data: dict) -> None:
    """
    Writes the given data to the json file at the given filepath.
    """
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding=ENCODING) as f:
        json.dump(data, f, indent=4)


def joblib_load(fp: str):
    """
    Load a joblib file.
    """
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    return joblib.load(fp)


def joblib_dump(data, fp: str):
    """
    Dump a joblib file.
    """
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    joblib.dump(data, fp)
