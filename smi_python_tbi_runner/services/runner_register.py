from runners import DEFAULT_RUNNER, BaseRunner


class RunnerRegisterService:

    def __init__(self):
        self.instances = {}

    def register(self, runner: BaseRunner):
        self.instances[runner.get_name()] = runner

    def get_runner(self, sub_command: str):
        return self.instances.get(sub_command, DEFAULT_RUNNER)
