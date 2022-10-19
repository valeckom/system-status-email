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
    print("get_sys_info.cmd_result:", cmd_result)

    matches = re.search(regex, cmd_result.stdout)

    if matches:
        res = matches.groupdict()
        print("get_sys_info.public:", res)
        return res


def get_uptime():
    cmd_result = subprocess.run(
        ["uptime", "-p"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print("get_sys_info.get_uptime.cmd_result:", cmd_result)

    up_time = cmd_result.stdout.lstrip("up")
    up_time = up_time.strip()

    print("get_sys_info.get_uptime:", up_time)
    return up_time


def get_zpool_info():
    res_dict = {
        "name": '-',
        "size": '-',
        "alloc": '-',
        "free": '-',
        "ckpoint": '-',
        "expandsz": '-',
        "frag": '-',
        "cap": '-',
        "dedup": '-',
        "health": '-',
        "altroot": '-',
    }

    try:
        cmd_result = subprocess.run(
            ["/sbin/zpool", 'list'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("get_zpool_info.cmd_result:", cmd_result)
    except Exception as e:
        print("get_zpool_info.ERROR: ", e)
        return res_dict

    regex = r"\n(?P<name>\S*)\s*(?P<size>\S*)\s*(?P<alloc>\S*)\s*(?P<free>\S*)\s*(?P<ckpoint>\S*)\s*(?P<expandsz>\S*)\s*(?P<frag>\S*)\s*(?P<cap>\S*)\s*(?P<dedup>\S*)\s*(?P<health>\S*)\s*(?P<altroot>\S*)"

    matches = re.search(regex, cmd_result.stdout)

    if not matches:
        return res_dict

    match_dict = matches.groupdict()
    print("get_zpool_info.match_dict:", match_dict)

    for res_dict_key in res_dict.keys():
        res_val = match_dict.get(res_dict_key)

        if res_val is not None:
            res_dict.update({res_dict_key: res_val})

    return res_dict


def get_sys_update_info():
    r = '-'

    try:
        cmd_result = subprocess.run(
            ["apt-get", "upgrade", "--dry-run"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("get_sys_update_info.cmd_result:", cmd_result)
    except Exception as e:
        print("get_sys_update_info.ERROR: ", e)
        return r

    regex = r"(?P<pendingUpgrades>\d*) upgraded, "

    matches = re.search(regex, cmd_result.stdout)

    if matches:
        res = matches.groupdict()
        print("get_sys_update_info.public:", res)
        r = res.get("pendingUpgrades")

    return r
