import datetime
from string import Template

from send_email import send_email
from system_info import get_sys_info, get_uptime, get_zpool_info, get_sys_update_info

uptime = get_uptime()
sys_info = get_sys_info()
zpool_info = get_zpool_info()
title_host_name = sys_info["hostname"].title()
pending_upgrades = get_sys_update_info()

date_obj = datetime.datetime.now()
date_str = date_obj.strftime("%c")

with open('message-template.html', 'r') as f:
    template_html_string = f.read()

t = Template(template_html_string)

html_string = t.substitute({
    "date": date_str,
    "title_hostname": title_host_name,
    "hostname": sys_info.get("hostname"),
    "operating_system": sys_info.get("os"),
    "kernel": sys_info.get("kernel"),
    "uptime": uptime,
    "size": zpool_info.get("size"),
    "free_space": zpool_info.get("free"),
    "fragmentation": zpool_info.get("frag"),
    "capacity": zpool_info.get("cap"),
    "health": zpool_info.get("health"),
    "pending_updates": pending_upgrades,
})

print("main.html_string:", html_string)

send_email(
    "mark86v@gmail.com",
    f"{title_host_name}'s Status Update",
    "Hello world!",
    html_string)
