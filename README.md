# pydep
A python package to display dependencies of functions

## Usage

Using the commands

```python
from source_examiner import SourceParser 
sp = SourceParser('./examples/')
sp.scan()
```

will return dictionaries for each file with all the functions defined and the set of functions they call within
their scope.

```python
{
    'example1': {
            'f': set(),
            'g': {'f'},
            'h': {'f', 'g', 's'},
            'Teste': set(),
            '__init__': set(),
            'method_a': set(),
            'method_b': {'f', 'method_a'}
        },
        'example2': {
            's': {'f'}
        }
}
```