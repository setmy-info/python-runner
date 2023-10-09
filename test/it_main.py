import unittest

from smi_python_tbi_runner.runner_application import main
from smi_python_tbi_runner.services.runner_register_service import runner_register_service
from test.runner_x import RunnerX


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
            '--sub-command', 'sub-x',
            '--tbi-file', './test/resources/tbi-376bdfaa-1195-11ee-be56-0242ac120002.yaml']
        result_collection = {'app': None, 'tbi_file': None, 'sub_command': None}
        runner_register_service.register(RunnerX(result_collection))
        result_code = main(args)
        self.assertEqual(result_code, 321)
        self.assertEqual(result_collection['sub_command'], 'sub-x')
        self.assertEqual(result_collection['app'].profiles_list, ['profile1', 'profile2'])
        self.assertEqual(result_collection['tbi_file'].get_name(), 'TBI name')


if __name__ == '__main__':
    unittest.main()
