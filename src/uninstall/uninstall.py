import os
from os.path import exists

from src.core.file_const import SYS_CRON_PATH
from src.load_info import get_info
from src.user_options import OPT_DRY_RUN


def uninstall():
    print(f"Uninstalling {get_info('display_name')}.")

    if os.environ.get(OPT_DRY_RUN):
        print("--dry-run: no changes will be made to the system")

    if exists(SYS_CRON_PATH):
        print(f"uninstall - removing file {SYS_CRON_PATH}")

        if os.environ.get('opt_dry_run'):
            print("Cron job removed.")
            return

        os.remove(SYS_CRON_PATH)
        print("Cron job removed.")
    else:
        print("No cron job detected.")

    print(f"You may now delete the source directory. `sudo rm -R {os.getcwd()}`")
