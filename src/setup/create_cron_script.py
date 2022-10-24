import os
import subprocess

from src.file_util import get_path

DEST = "/etc/cron.weekly/system_email"


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
    print(f"create_cron_script.write_file - writing {DEST}")

    if os.environ.get('opt_dry_run'):
        return

    with open(DEST, 'w') as f:
        print(f"create_cron_script - writing script to {DEST}")
        f.write(content)


def set_permissions():
    print(f"create_cron_script.set_permissions - Setting {DEST} permissions.")

    if os.environ.get('opt_dry_run'):
        return

    subprocess.run(
        ["chmod", "+x", DEST],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True)
