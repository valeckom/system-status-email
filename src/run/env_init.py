from os import environ
from os.path import exists
from re import findall, MULTILINE

from src.file_util import get_path

ENV_PATH = get_path(".env")
ENV_TEMPLATE_PATH = get_path("public/env-template.txt")
EXCEPTION = Exception(f"{ENV_PATH} does not exist. Run the install command " +
                      "to create it.")


def check_env_values():
    # Read the properties from the template
    with open(ENV_TEMPLATE_PATH, 'r') as f:
        template_string = f.read()

    regex = "^(.*)="
    matches = findall(regex, template_string, MULTILINE)

    # See if the properties have values in the .env file
    for prop in matches:
        v = environ.get(prop)

        if v == '':
            print(f"env_init.check_env_values.ERROR - {prop} is empty")
            raise EXCEPTION


def env_check():
    print("env_init.env_check - checking for a valid .env file")

    if exists(ENV_PATH):
        check_env_values()
    else:
        raise EXCEPTION
