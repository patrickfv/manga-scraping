from data.contracts.load_manga_repository import LoadMangaRepository
from data.models.manga import LoadMangaResult


class MangaHostRepository(LoadMangaRepository):
    def load_manga(self, name: str, **kwargs) -> list[LoadMangaResult]:
        pass
