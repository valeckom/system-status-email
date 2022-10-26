import os
import subprocess

from click import prompt

from src.core.file_cleanup import remove_any_previous_scripts
from src.core.file_const import SYS_CRON_PATHS
from src.file_util import get_path


def cron_script_install():
    remove_any_previous_scripts()

    content = read_cron_script_src()

    path = in_email_period()

    write_file(content, path)

    set_permissions(path)


def in_email_period():
    input_path_keys = {
        'h': 'hourly',
        'd': 'daily',
        'w': 'weekly',
        'm': 'monthly'
    }

    print("""How often do you want to send emails?
    h) Hourly
    d) Daily
    w) Weekly
    m) Monthly""")

    in_text = prompt(
        text='Select frequency',
        default='w',
        show_default=True,
        show_choices=True)

    key = input_path_keys.get(in_text)

    if key is None:
        print(f'Unknown response "{in_text}".')
        return in_email_period()

    return SYS_CRON_PATHS.get(key)


def read_cron_script_src():
    print(f"read_cron_script_src - Reading source file.")

    with open(get_path("public/cron-script.sh")) as f:
        content = f.read()

    return content


def write_file(content, path):
    print(f"create_cron_script.write_file - writing {path}")

    if os.environ.get('opt_dry_run'):
        return

    with open(path, 'w') as f:
        print(f"create_cron_script - writing script to {path}")
        f.write(content)


def set_permissions(path):
    print(f"create_cron_script.set_permissions - Setting {path} permissions.")

    if os.environ.get('opt_dry_run'):
        return

    subprocess.run(
        ["chmod", "+x", path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True)
