from os.path import normpath
from pathlib import Path
from sys import modules


def get_script_root():
    return Path(str(modules['__main__'].__file__)).parent


SCRIPT_ROOT = get_script_root()


def get_path(path_from_root):
    path = SCRIPT_ROOT.joinpath(path_from_root)
    return normpath(path)
