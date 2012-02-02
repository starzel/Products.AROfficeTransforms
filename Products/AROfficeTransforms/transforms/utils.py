import os

def command_exists(command):
    for path in os.environ["PATH"].split(os.pathsep):
        if os.path.exists(os.path.join(path, command)):
            return True
    else:
        return False