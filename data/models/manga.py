from domain.entities.manga import Manga, Page, Chapter


class PageModel(Page):
    pass


class ChapterModel(Chapter):
    def set_pages(self, page: PageModel | list[PageModel]):
        pass


class MangaModel(Manga):
    def set_chapter(self, chapter: ChapterModel | list[ChapterModel]):
        pass
