import shutil

import PyInstaller.__main__


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
        "system_email",
        "--add-data",
        "./public:public"
    ])


clean_paths()
do_build()
