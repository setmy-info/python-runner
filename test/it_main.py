import unittest

from runner_application import main
from runner_x import RunnerX
from services import runner_register_service


class ITExample(unittest.TestCase):

    def setUp(self):
        pass

    def test_main(self):
        args = [
            "something",
            '--smi-profiles', 'profile1,profile2',
            '--smi-config-paths', './test/resources',
            '--smi-optional-config-files', './test/resources/cli/optional.yaml',
            '--runner-command', 'runner-x',
            '--tbi-file', './test/resources/tbi-376bdfaa-1195-11ee-be56-0242ac120002.yaml']
        runner_register_service.register(RunnerX())
        main(args)


if __name__ == '__main__':
    unittest.main()
