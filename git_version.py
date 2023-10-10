import os
import subprocess

from smi_python_tbi_runner.project import NAME, VERSION

try:
    git_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode("utf-8")
    with open(os.path.join(os.path.dirname(__file__), NAME, 'project.py'), 'w') as file:
        file.write(f'NAME = "{NAME}"\n')
        file.write(f'VERSION = "{VERSION}"\n')
        file.write(f'HASH = "{git_hash}"\n')

except Exception as e:
    print(f"Error: {e}")
