import os
import re
from os.path import exists

ENV_PATH = "./.env"
EXCEPTION = Exception(".env is not complete. Check that all properties in .env are complete.")


def check_env_values():
    print("env_init.check_env_values - checking for valid .env")

    # Read the properties from the template
    with open("./public/env_template.txt", 'r') as f:
        template_string = f.read()

    regex = "^(.*)="
    matches = re.findall(regex, template_string, re.MULTILINE)

    # See if the properties have values in the .env file
    for prop in matches:
        v = os.environ.get(prop)

        if v == '':
            print(f"env_init.check_env_values.ERROR - {prop} is empty")
            raise EXCEPTION


def create_env_file():
    print("env_init.create_env_file - creating .env")

    with open("./public/env_template.txt", 'r') as f:
        template_string = f.read()

    with open(ENV_PATH, 'w') as f:
        f.write(template_string)


def env_init():
    print("env_init - checking for valid .env")
    file_exists = exists(ENV_PATH)

    if file_exists:
        check_env_values()
    else:
        create_env_file()
        raise EXCEPTION
