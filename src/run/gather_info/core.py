from re import finditer
from subprocess import run, PIPE


def parse_cmd(command: str, regex: str) -> list[dict[str, str]]:
    res = list()

    cmd_result = run(
        command.split(),
        stdout=PIPE,
        stderr=PIPE,
        text=True
    )

    matches = finditer(regex, cmd_result.stdout)

    for match in matches:
        res.append(match.groupdict())

    return res
