import os

import click
from dotenv import load_dotenv

from src.file_util import get_path
from src.install.install import install
from src.load_info import load_info, get_info
from src.run.run import run_system_email
from src.uninstall.uninstall import uninstall
from src.user_options import OPT_DRY_RUN, OPT_VERSION

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# Initialize the scripts global space
# This must happen before anything else
load_dotenv(dotenv_path=get_path(".env"))
load_info()


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.option("--dry-run",
              is_flag=True,
              default=False,
              help="Run the script without sending an email or writing files.")
@click.option("--version",
              "-v",
              is_flag=True,
              default=False,
              help="Show the version and exit.")
def main(dry_run, version):
    print(f"{get_info('display_name')}")
    print(f"version {get_info('version')}.{get_info('build_timestamp')}\n")

    if dry_run:
        os.environ[OPT_DRY_RUN] = OPT_DRY_RUN

    if version:
        os.environ[OPT_VERSION] = OPT_VERSION


@main.command(name="install")
def cmd_install():
    """Set up the script and add it to `cron.weekly`.
    """

    if os.environ.get(OPT_VERSION):
        return

    install()


@main.command(name="run")
def cmd_run():
    """Read the system information and send an email.
    """

    if os.environ.get(OPT_VERSION):
        return

    run_system_email()


@main.command(name="uninstall")
def cmd_uninstall():
    """Remove the script's system integration.
    """

    if os.environ.get(OPT_VERSION):
        return

    uninstall()


if __name__ == '__main__':
    main()
