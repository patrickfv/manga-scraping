from domain.entities.manga import Manga, Page, Chapter


class PageModel(Page):
    pass


class ChapterModel(Chapter):
    def set_pages(self, page: PageModel | list[PageModel]):
        super().set_pages(page) # type: ignore


class MangaModel(Manga):
    def set_chapter(self, chapter: ChapterModel | list[ChapterModel]):
        super().set_chapters(chapter) # type: ignore
