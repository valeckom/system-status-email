import os

from src.load_info import get_info
from src.setup.create_cron_script import create_cron_script


def setup():
    print(f"Installing or updating {get_info('display_name')}.")

    if os.environ.get('dry_run'):
        print("--dry-run: no changes will be made to the system")

    create_cron_script()
