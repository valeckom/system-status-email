from re import search
from subprocess import run, PIPE


def parse_cmd(command: str, regex: str) -> dict:
    cmd_result = run(
        command.split(),
        stdout=PIPE,
        stderr=PIPE,
        text=True
    )

    matches = search(regex, cmd_result.stdout)

    if matches:
        res = matches.groupdict()
        print(res)
        return res
