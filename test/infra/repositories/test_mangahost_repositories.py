import unittest
from unittest import TestCase, mock
from enum import Enum
import os, sys
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '../../..'))
from infra.repositories.manga_host import MangaHostRepository

class MangaHostConstants(Enum):
    SEARCH_NAME = 'kimetsu no yaba'
    SEARCH_RESULT = 9
    SEARCH_DOCUMENT_NAME = os.path.join(os.path.dirname(__file__), 'kimetsu_no_yaba_MangaHost.html')

class TestRepository(TestCase):

    def setUp(self) -> None:
        self.sut = MangaHostRepository()
        return super().setUp()

    def test_load_manga_search(self):
        doc_html = open(MangaHostConstants.SEARCH_DOCUMENT_NAME.value, 'r', encoding='utf-8')
        self.sut.get_doc_html = mock.MagicMock(return_value=doc_html)
        list = self.sut.load_manga(MangaHostConstants.SEARCH_NAME.value)
        self.assertEqual(len(list), MangaHostConstants.SEARCH_RESULT.value)


if __name__ == '__main__':
    unittest.main()