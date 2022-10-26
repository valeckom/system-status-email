from bs4 import BeautifulSoup, Tag


class TableCell:
    def __init__(self, content: str, is_header=False):
        self._is_header = is_header
        self._content = content

    def get_soup_tag(self, soup: BeautifulSoup) -> Tag:
        html_tag = 'th' if self._is_header else 'td'

        tag = soup.new_tag(html_tag)
        tag.append(self._content)

        return tag
