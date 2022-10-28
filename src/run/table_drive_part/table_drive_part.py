from src.core.table.table import Table
from src.core.table.table_cell import TableCell
from src.core.table.table_row import TableRow
from src.run.gather_info.core import parse_cmd


def get_table_drive_part() -> Table:
    info = get_drive_partition_info()

    template_map = {
        'Filesystem': 'filesystem',
        'Size': 'size',
        'Used': 'used',
        'Available': 'avail',
        'Use%': 'usepercent',
    }

    table = Table('Drive partition status')

    for title, content in template_map.items():
        row = TableRow()

        row.add_cell(TableCell(content=title, is_header=True))

        for item in info:
            item_value = item.get(content)
            cell = TableCell(content=item_value)
            row.add_cell(cell)

        table.add_row(row)

    return table


def get_drive_partition_info():
    regex = r"(?P<filesystem>/dev/sd.*?)\s+(?P<size>.*?\w)\s+(?P<used>.*?\w)\s+(?P<avail>.*?\w)\s+(?P<usepercent>.*?\w%)\s+(?P<mountpoint>.*?)\s"

    return parse_cmd("/usr/bin/df -h", regex)
