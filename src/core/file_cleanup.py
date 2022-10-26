from os import remove, environ
from os.path import exists

from src.core.file_const import SYS_CRON_PATHS


def remove_any_previous_scripts():
    print(f"remove_any_previous_scripts - cleaning up any previous cron " +
          "scripts.")

    for path in SYS_CRON_PATHS.values():
        if exists(path):
            if environ.get('opt_dry_run'):
                print(f"Cron job {path} removed.")
                continue

            remove(path)
            print(f"Cron job {path} removed.")
