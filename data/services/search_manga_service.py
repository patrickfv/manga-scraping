from domain.entities.manga import Manga
from domain.usecases.search_manga import SearchManga
from data.contracts.search_manga_repository import SearchMangaRepository


class SearchMangaService(SearchManga):

    def __init__(self, repository: SearchMangaRepository):
        self.repo = repository

    def load(self, name) -> list[Manga]:
        # middleman - code smell
        return self.repo.load_manga(name)
