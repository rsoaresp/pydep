import keyword
from io import BytesIO
from tokenize import tokenize, NAME
from typing import *


def find_functions(source_code: str) -> Dict[str, Set[str]]:

    functions, functions_names_found = dict(), list()
    tokens_generator = tokenize(BytesIO(source_code).readline)

    for token_type, token_string, _, _, _ in tokens_generator:

        if token_type == NAME and token_string in ['def', 'class']:
            next_token_type, next_token_string, _, _, _ = next(tokens_generator)

            if next_token_type == NAME:
                functions_names_found = []
                functions[next_token_string] = functions_names_found
        elif token_type == NAME and token_string not in keyword.kwlist:
            functions_names_found.append(token_string)

    functions_usage = move_to_set(functions)

    return functions_usage


def move_to_set(functions: Dict[str, List[str]]) -> Dict[str, Set[str]]:
    response = dict()
    for key, value in functions.items():
        response[key] = set(value)
    return response


def clean(relations: Dict[str, Dict[str, Set[str]]]) -> Dict[str, Dict[str, Set[str]]]:
    list_know_functions = list()
    for relations_dict in relations.values():
        list_know_functions += list(relations_dict.keys())

    cleaned_dict = dict()
    for file_name, relations_dict in relations.items():
        cleaned_dict[file_name] = dict()

        for key, value in relations_dict.items():
            cleaned_dict[file_name][key] = set()
            for i in value:
                if i in list_know_functions:
                    cleaned_dict[file_name][key].add(i)

    return cleaned_dict