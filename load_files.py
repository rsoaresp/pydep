import os
from typing import *


def get_source_code(path: str) -> Dict[str, str]:
    """Get all the source code passed by the user and store in a dictionary.

    It checks if the user has passed a single .py file or a directory containing multiple files and fetches all the
    source codes available. It returns a dictionary with keys being the names of the files (without the .py) and the
    values the source code.
    """
    source = dict()

    if os.path.isfile(path):
        if path.endswith('.py'):
            source.update(make_dict_entry(path))
    elif os.path.isdir(path) and any([i.endswith('.py') for i in os.listdir(path)]):
        for file_path in os.listdir(path):
            if file_path.endswith('.py'):
                full_file_path = os.path.join(path, file_path)
                source.update(make_dict_entry(full_file_path))

    return source


def make_dict_entry(path: str) -> Dict[str, str]:
    """Given a path to a file, read its content and returns a dictionary with file name and content (in utf-8)."""

    head, tail = os.path.split(path)
    with open(path, 'r') as file:
        entry = {tail.replace('.py', ''): file.read().encode('utf-8')}

    return entry