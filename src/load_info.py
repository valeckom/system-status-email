import json
import os

from src.file_util import get_path


def load_info():
    with open(get_path("info.json")) as f:
        os.environ["script_info"] = json.dumps(json.load(f))


def get_info(key):
    infos = os.environ.get("script_info")
    info = json.loads(infos)
    return info.get(key)
