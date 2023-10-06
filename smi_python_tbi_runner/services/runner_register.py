from runners import DEFAULT_RUNNER


class RunnerRegisterService:

    def __init__(self):
        self.instances = {}

    def get_runner(self, sub_command: str):
        return self.instances.get(sub_command, DEFAULT_RUNNER)
