from typing import *

from code_checker import find_functions, clean
from load_files import get_source_code


class SourceParser:

    def __init__(self, path: str):
        self.source_code = get_source_code(path)

    def scan(self) -> Dict[str, Dict[str, Set[str]]]:

        relations_dict = dict()
        for key, source in self.source_code.items():
            relations_dict[key] = find_functions(source)

        return clean(relations_dict)

    def diagram(self):
        pass