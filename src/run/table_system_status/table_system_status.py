from src.core.table.table import Table
from src.core.table.table_cell import TableCell
from src.core.table.table_row import TableRow
from src.run.gather_info.core import parse_cmd


def get_table_system_status() -> Table:
    sys_info = get_sys_info()
    uptime = get_uptime()
    upgrades = get_sys_update_info()

    template_map = {
        'Hostname': sys_info.get('hostname'),
        'Uptime': uptime.get('uptime'),
        'Pending upgrades': upgrades.get('pending_upgrades')
    }

    table = Table('System status')

    for title, content in template_map.items():
        row = TableRow()
        row.add_cell(TableCell(content=title, is_header=True))
        row.add_cell(TableCell(content=content))
        table.add_row(row)

    return table


def get_sys_info() -> dict:
    regex = r".*Static hostname: (?P<hostname>.*)(.|\s)*?Operating System: (?P<os>.*)(.|\s)*?Kernel: (?P<kernel>.*)"

    return parse_cmd("hostnamectl", regex)[0]


def get_uptime() -> dict:
    regex = r"up (?P<uptime>.*)"

    return parse_cmd("uptime -p", regex)[0]


def get_sys_update_info() -> dict:
    regex = r"(?P<pending_upgrades>\d*) upgraded, "

    return parse_cmd("apt-get upgrade --dry-run", regex)[0]
