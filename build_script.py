import shutil

import PyInstaller.__main__


def clean_paths():
    print("build_script.clean_paths")

    paths = ["./build", "./dist"]

    for path in paths:
        # Remove all directory content
        try:
            shutil.rmtree(path)
        except Exception as e:
            print("build_script.clean_paths - Error deleting directory")
            raise e


def do_build():
    print("build_script.do_build")

    PyInstaller.__main__.run([
        "--clean",
        "main.py",
        "--name",
        "system_email",
        "--add-data",
        "public:public"
    ])


clean_paths()
do_build()
