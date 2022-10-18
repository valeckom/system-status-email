import datetime
import os
from string import Template

from dotenv import load_dotenv

from src.env_init import env_init
from system_info import get_sys_info, get_uptime, get_zpool_info, get_sys_update_info

_ = load_dotenv()


def main():
    env_init()
    uptime = get_uptime()
    sys_info = get_sys_info()
    z_pool_info = get_zpool_info()
    title_host_name = sys_info["hostname"].title()
    pending_upgrades = get_sys_update_info()

    date_obj = datetime.datetime.now()
    date_str = date_obj.strftime("%c")

    with open('./public/message-template.html', 'r') as f:
        template_html_string = f.read()

    t = Template(template_html_string)

    html_string = t.substitute({
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
    })

    print("main.html_string:", html_string)

    print("to: ", os.environ.get("EMAIL_TO_ADDRESS"))

    # to_address = os.environ.get("EMAIL_TO_ADDRESS")

    # send_email(
    #     to_address,
    #     f"{title_host_name}'s Status Update",
    #     "Hello world!",
    #     html_string)


if __name__ == '__main__':
    main()
