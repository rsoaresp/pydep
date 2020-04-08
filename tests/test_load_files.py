import os
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

            self.paths[code_name] = self.files[code_name].name

        return None

    def tearDown(self) -> None:
        for file in self.files.values():
            file.close()

        return None

    def test_load_files_with_single_source_code(self):
        """Check if the function get_source_code returns a dict with the right key and value."""

        source_from_function = get_source_code(self.paths['code_a'])
        expected_dict = {os.path.split(self.paths['code_a'])[1].replace('.py', ''): self.codes['code_a']}

        self.assertDictEqual(source_from_function, expected_dict)
        return None

    def test_load_files_with_multiple_source_codes(self):
        """Check if the function get_source_code returns a dict with the right key and value for multiple files."""

        source_from_function = get_source_code(tempfile.gettempdir())
        expected_dict = {
                         os.path.split(self.paths['code_a'])[1].replace('.py', ''): self.codes['code_a'],
                         os.path.split(self.paths['code_b'])[1].replace('.py', ''): self.codes['code_b']
                        }
        self.assertDictEqual(source_from_function, expected_dict)
        return None