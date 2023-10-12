from smi_python_commons.config.application import Application
from smi_python_tbi_parser.tbi import Tbi


class RunnerX:

    def __init__(self, result_collection: dict):
        self.name = "runner-x"
        self.result_collection = result_collection

    def get_name(self):
        return self.name

    def execute(self, app: Application, sub_command: str):
        self.result_collection['app'] = app;
        self.result_collection['tbi_file'] = app.arguments.tbi_file;
        self.result_collection['sub_command'] = sub_command;
        self.result_collection['example'] = app.arguments.example;
        self.result_collection['name'] = app.name;
        return 321
