import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

from dotenv import load_dotenv

from system_info import get_sys_info, get_uptime, get_zpool_info, get_sys_update_info

_ = load_dotenv()


# From https://mljar.com/blog/python-send-email/
def send_email(to, subject, message, alt_html):
    try:
        email_address = os.environ.get("EMAIL_ADDRESS")
        email_password = os.environ.get("EMAIL_PASSWORD")

        if email_address is None or email_password is None:
            # no email address or password
            # something is not configured properly
            print("Did you set email address and password correctly?")
            return False

        # create email
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = email_address
        msg['To'] = to

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(message, 'plain')
        part2 = MIMEText(alt_html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
        return True
    except Exception as e:
        print("Problem during send email")
        print(str(e))
    return False


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
    f"{title_host_name}'s System Status",
    "Hello world!",
    html_string)
