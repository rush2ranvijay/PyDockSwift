import json
import sys

import pkg_resources


class PythonEnvironmentInfo(dict):
    def __init__(self):
        super().__init__()
        self['platform'] = sys.platform
        self['dependencies'] = []

    def add_dependency(self, dependency):
        self['dependencies'].append(dependency)


def run_it():
    info = PythonEnvironmentInfo()
    for ws in pkg_resources.working_set:
        info.add_dependency(str(ws.as_requirement()))
    return info


if __name__ == '__main__':
    print(json.dumps(run_it(), indent=4))
