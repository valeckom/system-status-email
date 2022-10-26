from bs4 import BeautifulSoup, Tag

from src.core.table.table_cell import TableCell


class TableRow:
    def __init__(self):
        self._cells = []

    def add_cell(self, cell: TableCell):
        self._cells.append(cell)

    def get_soup_tag(self, soup: BeautifulSoup) -> Tag:
        tag = soup.new_tag('tr')

        for cell in self._cells:
            cell_tag = cell.get_soup_tag(soup)
            tag.append(cell_tag)

        return tag
