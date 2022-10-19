import os
import sys
from pathlib import Path


def get_script_root():
    return Path(str(sys.modules['__main__'].__file__)).parent


SCRIPT_ROOT = get_script_root()


def get_path(path_from_root):
    path = SCRIPT_ROOT.joinpath(path_from_root)
    return os.path.normpath(path)
