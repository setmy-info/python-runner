from smi_python_commons.config.application import Application
from smi_python_tbi_parser.tbi import Tbi


class BaseRunner:

    def __init__(self):
        self.name = "default"

    def get_name(self):
        return self.name

    def execute(self, app: Application, tbi: Tbi):
        pass


DEFAULT_RUNNER = BaseRunner()
