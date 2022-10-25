import os

from src.install.create_cron_script import create_cron_script
from src.install.create_env_file import create_env_file
from src.load_info import get_info
from src.user_options import OPT_DRY_RUN


def install():
    print(f"Installing or updating {get_info('display_name')}.")

    if os.environ.get(OPT_DRY_RUN):
        print("--dry-run: no changes will be made to the system")

    create_env_file()
    create_cron_script()

    print("Installation is complete.")
