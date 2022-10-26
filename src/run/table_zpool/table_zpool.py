from src.core.table.table import Table
from src.core.table.table_cell import TableCell
from src.core.table.table_row import TableRow
from src.run.gather_info.core import parse_cmd


def get_table_zpool() -> Table:
    table = Table('ZPool status')

    info = get_zpool_info()

    template_map = {
        'Size': info.get('size'),
        'Free space': info.get('free'),
        'Capacity': info.get('cap'),
        'Health': info.get('health'),
    }

    for title, content in template_map.items():
        row = TableRow()
        row.add_cell(TableCell(content=title, is_header=True))
        row.add_cell(TableCell(content=content))
        table.add_row(row)

    return table


def get_zpool_info():
    regex = r"\n(?P<name>\S*)\s*(?P<size>\S*)\s*(?P<alloc>\S*)\s*(?P<free>\S*)\s*(?P<ckpoint>\S*)\s*(?P<expandsz>\S*)\s*(?P<frag>\S*)\s*(?P<cap>\S*)\s*(?P<dedup>\S*)\s*(?P<health>\S*)\s*(?P<altroot>\S*)"

    return parse_cmd("/sbin/zpool list", regex)
