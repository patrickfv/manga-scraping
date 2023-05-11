from domain.entities.manga import Manga
from domain.usecases.load_manga import LoadManga
from data.contracts.load_manga_repository import LoadMangaRepository


class LoadMangaService(LoadManga):

    def __init__(self, repository: LoadMangaRepository):
        self.repo = repository

    def load(self, identifier) -> Manga:
        # middleman - code smell
        return self.repo.load_manga(identifier)
