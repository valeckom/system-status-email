import json
import os
import shutil
import tarfile
import time

import PyInstaller.__main__

INFO_FILENAME = "info.json"
README_FILENAME = "README.md"


def clean_paths():
    """Remove build directories;

    insuring our new build does not contain any old  build artifacts.
    """
    paths = ["./build", "./dist"]

    for path in paths:
        print(f"build_script.clean_paths - deleting {path}")
        shutil.rmtree(path, ignore_errors=True)


def do_build():
    PyInstaller.__main__.run([
        "--clean",
        "./main.py",
        "--name",
        build_info["name"],
        "--add-data",
        "./public:public",
    ])


def make_tarfile():
    output_filename = f"./dist/{build_info.get('name')}.tar.gz"
    source_dir = f"./dist/{build_info.get('name')}"

    with tarfile.open(output_filename, "w:gz") as tar:
        dest_path = os.path.basename(source_dir)
        print(f"make_tarfile - adding {source_dir} to {output_filename}")
        tar.add(source_dir, arcname=dest_path)


def get_build_info() -> dict:
    """
    Read info.json and make the values available to the rest of the script.
    """
    with open(f"./{INFO_FILENAME}") as f:
        info = json.load(f)

    info["build_timestamp"] = int(time.time())

    print(f"gen_build_info.info: {info}")

    return info


def gen_dist_info():
    print(f"gen_dist_info.build_info: {build_info}")

    with open(f"./dist/{build_info.get('name')}/{INFO_FILENAME}", 'w') as f:
        f.write(json.dumps(build_info))


def gen_readme():
    readme_name = "README.txt"

    print(f"gen_readme - Generating {readme_name}")

    shutil.copyfile('README.md', f'dist/{build_info.get("name")}/{readme_name}')


build_info = get_build_info()
clean_paths()
do_build()
gen_dist_info()
gen_readme()
make_tarfile()
