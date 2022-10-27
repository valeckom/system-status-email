from os import environ
from re import sub

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

    sys_info = get_sys_info()
    title_host_name = sys_info.get('hostname').title()
    title_host_name = f'{title_host_name}\'s update'

    plain_text += f'{title_host_name}\n\n'

    with open(get_path('public/message_template.html')) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    header_tag = soup.new_tag('h2')
    header_tag.string = title_host_name
    soup.body.append(header_tag)

    append_table(get_table_system_status)
    append_table(get_table_drive_part)
    append_table(get_table_zpool)

    min_html = minify_html(str(soup))

    print(min_html)
    print(plain_text)

    to_address = environ.get("EMAIL_TO_ADDRESS")

    send_email(
        to_address,
        f"{title_host_name}'s Status Update",
        plain_text,
        min_html)

    print(f"{get_info('display_name')} completed successfully.")


def minify_html(html: str) -> str:
    """Remove whitespace in the HTML"""

    regex = r"\n\s*"

    return sub(regex, '', html, 0)
