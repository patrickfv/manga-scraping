from data.models.manga import LoadMangaResult


class SearchMangaRepository:

    def search_manga(self, name: str, **kwargs) -> list[LoadMangaResult]:
        pass
