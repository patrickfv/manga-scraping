from domain.entities.manga import Manga, Page, Chapter


class PageParams(Page):
    pass


class ChapterParams(Chapter):
    def set_pages(self, page: PageParams | list[PageParams]):
        super().set_pages(page)


class LoadMangaResult(Manga):
    def set_chapter(self, chapter: ChapterParams | list[ChapterParams]):
        super().set_chapters(chapter)

