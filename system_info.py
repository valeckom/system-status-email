import re
import subprocess


def get_sys_info():
    regex = r".*Static hostname: (?P<hostname>.*)(.|\s)*?Operating System: (?P<os>.*)(.|\s)*?Kernel: (?P<kernel>.*)"

    cmd_result = subprocess.run(
        ["hostnamectl"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    matches = re.search(regex, cmd_result.stdout)

    if matches:
        res = matches.groupdict()
        print("get_sys_info.res:", res)
        return res


def get_uptime():
    cmd_result = subprocess.run(
        ["uptime", "-p"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print("get_uptime.cmd_result:", cmd_result)
    up_time = cmd_result.stdout.lstrip("up")
    up_time = up_time.strip()

    print("get_sys_info.up_time:", up_time)
    return up_time
