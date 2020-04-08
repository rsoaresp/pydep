import keyword
from io import BytesIO
from tokenize import tokenize, NAME, NEWLINE
from typing import *


def find_imports(source_code: str) -> List[str]:

    functions_imports = list()
    tokens_generator = tokenize(BytesIO(source_code).readline)

    for token_type, token_string, _, _, _ in tokens_generator:
        if token_string == 'import':
            next_token_type, next_token_string, _, _, _ = next(tokens_generator)

            while next_token_type != NEWLINE:
                functions_imports.append(next_token_string)
                next_token_type, next_token_string, _, _, _ = next(tokens_generator)

    return functions_imports


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
    """Remove tokens that are not function definitions."""

    list_know_functions, function_def_origin = get_list_know_function(relations)

    cleaned_dict = dict()
    for file_name, relations_dict in relations.items():
        cleaned_dict[file_name] = dict()

        for function, value in relations_dict.items():
            cleaned_dict[file_name][function] = set()
            for i in value:
                if i in list_know_functions:
                    if function_def_origin[i] != file_name:
                        cleaned_dict[file_name][function].add(f'{function_def_origin[i]}.{i}')
                    else:
                        cleaned_dict[file_name][function].add(f'{i}')

    return cleaned_dict


def get_list_know_function(relations: Dict[str, Dict[str, Set[str]]]) -> Tuple[List[str], Dict[str, str]] :
    """Returns a list with all the functions discovered on the source files."""

    list_know_functions = list()
    function_def_origin = dict()

    for file_name, relations_dict in relations.items():
        list_know_functions += list(relations_dict.keys())

        for function in relations_dict.keys():
            function_def_origin[function] = file_name

    return list_know_functions, function_def_origin