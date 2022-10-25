import os
import subprocess

from src.core.file_const import SYS_CRON_PATH
from src.file_util import get_path


def create_cron_script():
    content = read_cron_script_src()

    write_file(content)

    set_permissions()


def read_cron_script_src():
    print(f"create_cron_script.read_cron_script_src - Reading source file.")

    with open(get_path("public/cron-script.txt")) as f:
        content = f.read()

    return content


def write_file(content):
    print(f"create_cron_script.write_file - writing {SYS_CRON_PATH}")

    if os.environ.get('opt_dry_run'):
        return

    with open(SYS_CRON_PATH, 'w') as f:
        print(f"create_cron_script - writing script to {SYS_CRON_PATH}")
        f.write(content)


def set_permissions():
    print(f"create_cron_script.set_permissions - Setting {SYS_CRON_PATH} permissions.")

    if os.environ.get('opt_dry_run'):
        return

    subprocess.run(
        ["chmod", "+x", SYS_CRON_PATH],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True)
