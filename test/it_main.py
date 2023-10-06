import unittest

from main import main


class ITExample(unittest.TestCase):

    def setUp(self):
        pass

    def test_main(self):
        args = [
            "something",
            '--smi-profiles', 'profile1,profile2',
            '--smi-config-paths', './test/resources',
            '--smi-optional-config-files', './test/resources/cli/optional.yaml',
            '--sub-command', 'default',
            '--tbi-file', './test/resources/tbi-376bdfaa-1195-11ee-be56-0242ac120002.yaml']
        main(args)


if __name__ == '__main__':
    unittest.main()
