from os import environ

from bs4 import BeautifulSoup

from src.file_util import get_path
from src.load_info import get_info
from src.run.env_init import env_check
from src.run.send_email import send_email
from src.run.table_drive_part.table_drive_part import get_table_drive_part
from src.run.table_system_status.table_system_status import get_table_system_status, get_sys_info
from src.run.table_zpool.table_zpool import get_table_zpool
from src.user_options import OPT_DRY_RUN


def run_system_email():
    plain_text = ''

    def append_table(table_func):
        """Add the table to the HTML and Plain Text content."""

        nonlocal plain_text
        nonlocal soup

        try:
            table = table_func()

            tag = table.get_soup_tag(soup)
            soup.body.append(tag)

            plain_text += table.get_plain_text()
        except Exception as e:
            print(e)

    if environ.get(OPT_DRY_RUN):
        print("--dry-run: No email will be sent.\n")

    env_check()

    plain_text = ''

    sys_info = get_sys_info()
    title_host_name = sys_info.get('hostname').title()

    plain_text += f'{title_host_name}\'s update\n\n'

    with open(get_path('public/message_template.html')) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    try:
        system_table = get_table_system_status()

        system_soup_tag = system_table.get_soup_tag(soup)
        soup.body.append(system_soup_tag)

        plain_text += system_table.get_plain_text()
    except Exception as e:
        print(e)

    try:
        drive_table = get_table_drive_part()

        drive_soup_tag = drive_table.get_soup_tag(soup)
        soup.body.append(drive_soup_tag)

    append_table(get_table_system_status)
    append_table(get_table_drive_part)
    append_table(get_table_zpool)

    try:
        zpool_table = get_table_zpool()

        zpool_soup_tag = zpool_table.get_soup_tag(soup)
        soup.body.append(zpool_soup_tag)

        plain_text += zpool_table.get_plain_text()
    except Exception as e:
        print(e)

    print(soup.prettify())
    print(plain_text)

    to_address = environ.get("EMAIL_TO_ADDRESS")

    send_email(
        to_address,
        f"{title_host_name}'s Status Update",
        plain_text,
        str(soup))

    print(f"{get_info('display_name')} completed successfully.")
