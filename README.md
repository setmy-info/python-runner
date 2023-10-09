# python-tbi-runner

Training Backlog Item file parser

## Development

### Preparations

```shell
py -3.9 -m venv ./.venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

For developing depending project/module, dependency can be added into **requirements.txt** as:

    python-commons @ file:///C:/sources/setmy.info/submodules/python-commons

### PyCharm

"File" -> "Settings" -> Python Integrated Tools -> Default test runner: Unittest

Running tests have a problem: working directory has to be set for tests.

### Run unit tests

```shell
python -m unittest discover -s ./test
```

### Run integration tests

```shell
python -m unittest discover -s ./test -p it_*.py
```

### All tests

```shell
python -m unittest discover -s ./test && python -m unittest discover -s ./test -p it_*.py
```

## Deploy

```shell
python setup.py sdist bdist_wheel
twine upload dist/*
```

```shell
python setup.py sdist bdist_wheel && twine upload dist/*
```

## Usage

```python
import sys
from smi_python_tbi_runner.runner_application import main
from smi_python_tbi_runner.services.runner_register_service import runner_register_service
from your_code.runner_x import RunnerX

if __name__ == "__main__":
    runner_register_service.register(RunnerX())
    sys.exit(main(sys.argv))
```
