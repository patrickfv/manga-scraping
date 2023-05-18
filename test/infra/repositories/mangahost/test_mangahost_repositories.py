import unittest, os, sys, configparser
from unittest import TestCase, mock
from enum import Enum
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '../../../..'))
from infra.repositories.manga_host import MangaHostRepository
from data.models.manga import LoadMangaResult

class MangaHostConstants(Enum):
    SEARCH_DOCUMENT_NAME = os.path.join(os.path.dirname(__file__), 'doc/kimetsu_no_yaba_mangahost.html')
    MANGA_DOCUMENT_NAME = os.path.join(os.path.dirname(__file__), 'doc/dr.stone_mangahost.html')
    ENV = os.path.join(os.path.dirname(__file__), 'doc/.env')

class TestMangaRepository(TestCase):

    def setUp(self) -> None:
        self.sut: MangaHostRepository = MangaHostRepository()
        self.env = configparser.ConfigParser()
        self.env.read(MangaHostConstants.ENV.value, encoding='utf-8')
        return super().setUp()

    def test_search_manga(self):
        doc_html = open(MangaHostConstants.SEARCH_DOCUMENT_NAME.value, 'r', encoding='utf-8')
        self.sut.get_doc_html = mock.MagicMock(return_value=doc_html)
        result: list[LoadMangaResult] = self.sut.search_manga('')
        self.assertEqual(len(result), int(self.env['test_search_manga']['EXPECTED']))

    def test_load_manga(self):
        doc_html = open(MangaHostConstants.MANGA_DOCUMENT_NAME.value, 'r', encoding='utf-8')
        self.sut.get_doc_html = mock.MagicMock(return_value=doc_html)
        result: LoadMangaResult = self.sut.load_manga('')
        self.assertIsInstance(result, LoadMangaResult)
        self.assertEqual(len(result.chapters), int(self.env['test_load_manga']['CHAPTERS_EXPECTED']))
        self.assertEqual(result.author, self.env['test_load_manga']['AUTHOR_EXPECTED'])
        self.assertTrue(result.status)
        self.assertEqual(result.description, self.env['test_load_manga']['DESCRIPTION_EXPECTED'])


if __name__ == '__main__':
    unittest.main()