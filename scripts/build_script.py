import os
import shutil
import tarfile

import PyInstaller.__main__

PACKAGE_NAME = "system_email"


def clean_paths():
    paths = ["./build", "./dist"]

    for path in paths:
        print(f"build_script.clean_paths - deleting {path}")
        shutil.rmtree(path, ignore_errors=True)


def do_build():
    print("build_script.do_build")

    PyInstaller.__main__.run([
        "--clean",
        "./main.py",
        "--name",
        PACKAGE_NAME,
        "--add-data",
        "./public:public",
        "--add-data",
        "./README.md:.",
    ])


def make_tarfile():
    output_filename = f"./dist/{PACKAGE_NAME}.tar.gz"
    source_dir = f"./dist/{PACKAGE_NAME}"

    with tarfile.open(output_filename, "w:gz") as tar:
        dest_path = os.path.basename(source_dir)
        print(f"make_tarfile - adding {source_dir} to {output_filename}")
        tar.add(source_dir, arcname=dest_path)


clean_paths()
do_build()
make_tarfile()
