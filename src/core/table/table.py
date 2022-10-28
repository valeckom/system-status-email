from bs4 import BeautifulSoup
from prettytable import PrettyTable

from src.core.html_const import COLOR
from src.core.table.table_row import TableRow


class Table:
    def __init__(self, header: str):
        self._header = header
        self._rows = []

    def add_row(self, row: TableRow):
        self._rows.append(row)

    def get_soup_tag(self, soup: BeautifulSoup):
        header_tag = soup.new_tag('h3')
        header_tag.append(self._header)

        table_tag = soup.new_tag('table')

        for row in self._rows:
            row_tag = row.get_soup_tag(soup)
            table_tag.append(row_tag)

        div_tag = soup.new_tag('div')
        div_tag['style'] = f'color: {COLOR}'
        div_tag.append(header_tag)
        div_tag.append(table_tag)

        return div_tag

    def get_plain_text(self):
        table = PrettyTable()
        table.align = 'l'
        table.header = False

        for row in self._rows:
            table.add_row(row.get_content_list())

        return table.get_string(title=self._header) + '\n'
