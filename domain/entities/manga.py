class Page:
    def __init__(self, index: int, path: str):
        self.path = path
        self.index = index


class Manga:
    pages: list[Page] = []
    author: str = ''
    description: str = ''
    categories: dict[str, str] = {}

    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path

    def get_pages(self):
        return self.pages

    def set_pages(self, pages: Page | list[Page]):
        if isinstance(pages, Page):
            self.pages.append(pages)
        if isinstance(pages, list):
            self.pages.extend(pages)
