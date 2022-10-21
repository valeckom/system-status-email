import datetime
import os
from string import Template

import click
from dotenv import load_dotenv

from src.env_init import env_init
from src.file_util import get_path
from src.load_info import load_info, get_info
from src.send_email import send_email
from src.setup.setup import setup
from src.system_info import get_sys_info, get_uptime, get_zpool_info, get_sys_update_info, get_drive_partition_info

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# Initialize the scripts global space
# This must happen before anything else
load_dotenv(dotenv_path=get_path(".env"))
load_info()


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("--dry-run",
              "-d",
              is_flag=True,
              default=False,
              help="Run the script without sending an email.")
@click.option("--install",
              "-i",
              is_flag=True,
              default=False,
              help="Install/Update the script into the system. "
                   "Using this option requires elevated privileges.")
@click.option("--version",
              "-v",
              is_flag=True,
              default=False,
              help="Show the version and exit.")
def main(dry_run, install, version):
    print(f"{get_info('display_name')}")
    print(f"version {get_info('version')}.{get_info('build_timestamp')}\n")

    if dry_run:
        os.environ['dry_run'] = 'dry_run'

    if version:
        return

    if install:
        setup()
        return

    if dry_run:
        print("--dry-run: No email will be sent.\n")

    env_init()
    uptime = get_uptime()
    sys_info = get_sys_info()
    z_pool_info = get_zpool_info()
    drive_info = get_drive_partition_info()
    title_host_name = sys_info["hostname"].title()
    pending_upgrades = get_sys_update_info()

    date_obj = datetime.datetime.now()
    date_str = date_obj.strftime("%c")

    template_mapping = {
        "date": date_str,
        "title_hostname": title_host_name,
        "hostname": sys_info.get("hostname"),
        "operating_system": sys_info.get("os"),
        "kernel": sys_info.get("kernel"),
        "uptime": uptime,
        "size": z_pool_info.get("size"),
        "free_space": z_pool_info.get("free"),
        "fragmentation": z_pool_info.get("frag"),
        "capacity": z_pool_info.get("cap"),
        "health": z_pool_info.get("health"),
        "pending_updates": pending_upgrades,
        "drive_filesystem": drive_info.get("filesystem"),
        "drive_size": drive_info.get("size"),
        "drive_used": drive_info.get("used"),
        "drive_avail": drive_info.get("avail"),
        "drive_use_percent": drive_info.get("usepercent"),
    }

    with open(get_path("public/message-template.html"), 'r') as f:
        template_html_string = f.read()

    t = Template(template_html_string)

    html_string = t.substitute(template_mapping)

    with open(get_path("public/message-template.txt"), 'r') as f:
        template_text_string = f.read()

    t = Template(template_text_string)

    text_string = t.substitute(template_mapping)

    print("main:text_string:", text_string)

    to_address = os.environ.get("EMAIL_TO_ADDRESS")

    send_email(
        to_address,
        f"{title_host_name}'s Status Update",
        text_string,
        html_string)

    print(f"{get_info('display_name')} completed successfully.")


if __name__ == '__main__':
    main()
