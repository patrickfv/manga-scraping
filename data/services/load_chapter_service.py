from domain.entities.manga import Chapter
from domain.usecases.load_chapter import LoadChapter
from data.contracts.load_chapter_repository import LoadChapterRepository


class LoadChapterService(LoadChapter):

    def __init__(self, repo: LoadChapterRepository) -> None:
        self.repo = repo

    def load(self, identifier) -> Chapter:
        return self.repo.load_chapter(identifier)