from domain.entities.manga import Manga, Page


class PageParams(Page):
    pass


class LoadMangaResult(Manga):
    def set_pages(self, pages: PageParams | list[PageParams]):
        super().set_pages(pages)

