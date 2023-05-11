import unittest
from unittest import TestCase, mock
from enum import Enum
import os, sys
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '../../..'))
from infra.repositories.manga_host import MangaHostRepository
from data.contracts.search_manga_repository import SearchMangaRepository
from data.models.manga import LoadMangaResult


class MangaHostConstants(Enum):
    SEARCH_NAME = 'kimetsu no yaba'
    SEARCH_RESULT = 9
    SEARCH_DOCUMENT_NAME = os.path.join(os.path.dirname(__file__), 'kimetsu_no_yaba_mangahost.html')
    MANGA_DOCUMENT_NAME = os.path.join(os.path.dirname(__file__), 'dr.stone_mangahost.html')

class TestRepository(TestCase):

    def setUp(self) -> None:
        self.sut: SearchMangaRepository = MangaHostRepository()
        return super().setUp()

    def test_load_manga_search(self):
        doc_html = open(MangaHostConstants.SEARCH_DOCUMENT_NAME.value, 'r', encoding='utf-8')
        self.sut.get_doc_html = mock.MagicMock(return_value=doc_html)
        result: list[LoadMangaResult] = self.sut.search_manga(MangaHostConstants.SEARCH_NAME.value)
        self.assertEqual(len(result), MangaHostConstants.SEARCH_RESULT.value)
    '''
    def test_load_manga(self):
        doc_html = open(MangaHostConstants.MANGA_DOCUMENT_NAME.value, 'r', encoding='utf-8')
        self.sut.get_doc_html = mock.MagicMock(return_value=doc_html)
    '''

if __name__ == '__main__':
    unittest.main()