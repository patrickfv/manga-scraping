from data.models.manga import MangaModel


class SearchMangaRepository:

    def search_manga(self, name: str, **kwargs) -> list[MangaModel]: # type: ignore
        pass
