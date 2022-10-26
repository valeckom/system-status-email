from os import environ, getcwd

from src.core.file_cleanup import remove_any_previous_scripts
from src.load_info import get_info
from src.user_options import OPT_DRY_RUN


def uninstall():
    print(f"Uninstalling {get_info('display_name')}.")

    if environ.get(OPT_DRY_RUN):
        print("--dry-run: no changes will be made to the system")

    remove_any_previous_scripts()

    print(f"You may now delete the source directory. `sudo rm -R {getcwd()}`")
