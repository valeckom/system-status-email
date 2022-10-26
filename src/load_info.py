from json import dumps, load, loads
from os import environ

from src.file_util import get_path


def load_info():
    with open(get_path("info.json")) as f:
        environ["script_info"] = dumps(load(f))


def get_info(key):
    infos = environ.get("script_info")
    info = loads(infos)
    return info.get(key)
