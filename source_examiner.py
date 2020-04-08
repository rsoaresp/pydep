from typing import *

from code_checker import find_functions, find_imports, clean
from load_files import get_source_code


class SourceParser:

    def __init__(self, path: str):
        self.source_code = get_source_code(path)

    def scan(self) -> Dict[str, Dict[str, Set[str]]]:

        relations_dict = dict()
        for file_name, source in self.source_code.items():
            imports = find_imports(source)

            response = dict()
            for key, value in find_functions(source).items():
                response[key] = {i if (i in imports or i in find_functions(source).keys()) else None for i in value}

            relations_dict[file_name] = response

        return clean(relations_dict)

    def diagram(self):
        pass