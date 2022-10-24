import os
from os.path import exists
from string import Template

import click

from src.file_util import get_path
from src.user_options import OPT_DRY_RUN

FILE_PATH = get_path(".env")


def create_env_file():
    if exists(FILE_PATH):
        if in_should_use_old_env():
            return

    template_map = {
        "from_email": in_from_email_address(),
        "email_password": in_email_password(),
        "to_email": in_to_email_address()
    }

    content = gen_env_file_content(template_map)

    write_env_file(content)


def in_should_use_old_env():
    return click.confirm('A previous configuration was found. Do you want to use it?')


def in_from_email_address():
    return click.prompt("Enter the email address that will be sending the email")


def in_email_password():
    return click.prompt("Enter the email account password")


def in_to_email_address():
    return click.prompt("Enter the email address that you want the email to go to")


def gen_env_file_content(template_map):
    with open(get_path("public/env-template.txt"), 'r') as f:
        template_html_string = f.read()

    t = Template(template_html_string)

    return t.substitute(template_map)


def write_env_file(content):
    print("create_env_file.create_env_file - writing .env")

    if os.environ.get(OPT_DRY_RUN):
        return

    with open(FILE_PATH, 'w') as f:
        f.write(content)
