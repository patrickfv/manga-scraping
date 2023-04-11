from domain.entities.manga import Manga


class LoadManga:
    def load(self, identifier: str) -> list[Manga]:
        return [Manga('LoadMangaResult', '')]
