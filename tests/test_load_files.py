import os
import collections
import unittest
import tempfile

from load_files import get_source_code


class LoaderTester(unittest.TestCase):

    def setUp(self) -> None:

        self.codes = {
            'code_a': b"def f(x)\nreturn x\ndef g(x)\nreturn x + f(x)",
            'code_b': b"def h(x)\nreturn x\ndef k(x)\nreturn x + h(x)"
        }

        self.files, self.paths = dict(), dict()
        for code_name, source_code in self.codes.items():
            self.files[code_name] = tempfile.NamedTemporaryFile(suffix='.py')
            self.files[code_name].write(source_code)
            self.files[code_name].seek(0)

            self.paths[code_name] = self.path_spliter(self.files[code_name].name)

        return None

    def tearDown(self) -> None:
        for file in self.files.values():
            file.close()

        return None

    @staticmethod
    def path_spliter(x):
        return (x, *os.path.split(x))

    def test_load_files_with_single_source_code(self):
        """Check if the function get_source_code returns a dict with the right key and value."""

        source_from_function = get_source_code(self.paths['code_a'][0])
        expected_dict = {self.paths['code_a'][2].replace('.py', ''): self.codes['code_a']}

        self.assertDictEqual(source_from_function, expected_dict)
        return None

    def test_load_files_with_multiple_source_codes(self):
        """Check if the function get_source_code returns a dict with the right key and value for multiple files."""

        source_from_function = get_source_code(tempfile.gettempdir())
        expected_dict = {
            self.paths['code_a'][2].replace('.py', ''): self.codes['code_a'],
            self.paths['code_b'][2].replace('.py', ''): self.codes['code_b']
        }
        self.assertDictEqual(source_from_function, expected_dict)
        return None
