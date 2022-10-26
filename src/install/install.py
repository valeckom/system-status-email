import os

from src.install.cron_script_install import cron_script_install
from src.install.env_file_install import env_file_install
from src.load_info import get_info
from src.user_options import OPT_DRY_RUN


def install():
    print(f"Installing or updating {get_info('display_name')}.")

    if os.environ.get(OPT_DRY_RUN):
        print("--dry-run: no changes will be made to the system")

    env_file_install()
    cron_script_install()

    print("Installation is complete.")
