import datetime
import os
from string import Template

from src.file_util import get_path
from src.load_info import get_info
from src.run.drive_info import get_drive_partition_info
from src.run.env_init import env_check
from src.run.send_email import send_email
from src.run.system_info import get_uptime, get_zpool_info, get_sys_info, get_sys_update_info
from src.user_options import OPT_DRY_RUN


def run_system_email():
    if os.environ.get(OPT_DRY_RUN):
        print("--dry-run: No email will be sent.\n")

    env_check()
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
