from re import search
from subprocess import run, PIPE


def get_drive_partition_info():
    res_dict = {
        "filesystem": '-',
        "size": '-',
        "used": '-',
        "avail": '-',
        "usepercent": '-',
        "mountpoint": '-',
    }

    try:
        cmd_result = run(
            ["/usr/bin/df", '-h'],
            stdout=PIPE,
            stderr=PIPE,
            text=True
        )
        print("get_drive_partition_info.cmd_result:", cmd_result)
    except Exception as e:
        print("get_zpool_info.ERROR: ", e)
        return res_dict

    regex = r"(?P<filesystem>/dev/sd.*?)\s+(?P<size>.*?\w)\s+(?P<used>.*?\w)\s+(?P<avail>.*?\w)\s+(?P<usepercent>.*?\w%)\s+(?P<mountpoint>.*?)\s"

    matches = search(regex, cmd_result.stdout)

    if not matches:
        return res_dict

    match_dict = matches.groupdict()
    print("get_drive_partition_info.match_dict:", match_dict)

    for res_dict_key in res_dict.keys():
        res_val = match_dict.get(res_dict_key)

        if res_val is not None:
            res_dict.update({res_dict_key: res_val})

    return res_dict
