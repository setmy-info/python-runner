from smi_python_commons.arguments.argument import Argument
from smi_python_commons.arguments.config import Config
from smi_python_commons.arguments.constants import SMI_PROFILES_ARGUMENT, SMI_CONFIG_PATHS_ARGUMENT, \
    SMI_OPTIONAL_CONFIG_FILES_ARGUMENT
from smi_python_commons.config.application import Application
from smi_python_tbi_parser.tbi import parse_tbi

from services import runner_register_service


def main(argv):
    argv_config = Config(
        'TBI runner',
        [
            SMI_PROFILES_ARGUMENT,
            SMI_CONFIG_PATHS_ARGUMENT,
            SMI_OPTIONAL_CONFIG_FILES_ARGUMENT,
            Argument('runner-command', 'r', str, 'Runner to be executed', True),
            Argument('tbi-file', 't', str, 'TBI yaml to be used', True)
        ])
    app = Application(argv, argv_config)
    runner = runner_register_service.get_runner(app.arguments.runner_command)
    tbi = parse_tbi(app.arguments.tbi_file)
    runner.execute(app, tbi)


'''
import sys
from smi_python_tbi_runner.runner_application import main
from smi_python_tbi_runner.services import runner_register_service

if __name__ == "__main__":
    runner_register_service.register(RunnerX())
    main(sys.argv)
'''
