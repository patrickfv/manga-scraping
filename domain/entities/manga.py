class Page:
    def __init__(self, chapter, index: int, path: str):
        self.chapter = chapter
        self.path = path
        self.index = index


class Chapter:
    pages: list[Page]

    def __init__(self, manga, number: int, title: str, path: str):
        self.manga = manga
        self.number = number
        self.title = title
        self.path = path

    def set_pages(self, page: Page | list[Page]):
        if isinstance(page, Page):
            self.pages.append(page)
        if isinstance(page, list):
            self.pages.extend(page)


class Manga:
    chapters: list[Chapter] = []
    author: str = ''
    description: str = ''
    categories: list = []
    picture = None

    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path

    def get_chapter(self):
        return self.chapters

    def set_chapters(self, chapter: Chapter | list[Chapter]):
        if isinstance(chapter, Chapter):
            self.chapters.append(chapter)
        if isinstance(chapter, list):
            self.chapters.extend(chapter)

    def __str__(self):
        return '%s: %s' % (self.name, self.path)
