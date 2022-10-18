import shutil

import PyInstaller.__main__


def clean_paths():
    print("build_script.clean_paths")

    paths = ["./build", "./dist"]

    for path in paths:
        # Remove all directory content
        try:
            shutil.rmtree(path)
        except:
            print("build_script.clean_paths - Error deleting directory")


def do_build():
    print("build_script.do_build")

    PyInstaller.__main__.run([
        "--clean",
        "./app/main.py",
        "--name",
        "system_email",
        "--add-data",
        "./app/public:public"
    ])


clean_paths()
do_build()
