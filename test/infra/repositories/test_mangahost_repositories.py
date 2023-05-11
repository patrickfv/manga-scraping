import unittest
from unittest import TestCase, mock
from enum import Enum
import os, sys
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, '../../..'))
from infra.repositories.manga_host import MangaHostRepository
from data.models.manga import LoadMangaResult


class MangaHostConstants(Enum):
    SEARCH_DOCUMENT_NAME = os.path.join(os.path.dirname(__file__), 'kimetsu_no_yaba_mangahost.html')
    MANGA_DOCUMENT_NAME = os.path.join(os.path.dirname(__file__), 'dr.stone_mangahost.html')

class TestRepository(TestCase):

    def setUp(self) -> None:
        self.sut: MangaHostRepository = MangaHostRepository()
        return super().setUp()

    def test_load_manga_search(self):
        doc_html = open(MangaHostConstants.SEARCH_DOCUMENT_NAME.value, 'r', encoding='utf-8')
        self.sut.get_doc_html = mock.MagicMock(return_value=doc_html)
        result: list[LoadMangaResult] = self.sut.search_manga('')
        self.assertEqual(len(result), 9)

    def test_load_manga(self):
        doc_html = open(MangaHostConstants.MANGA_DOCUMENT_NAME.value, 'r', encoding='utf-8')
        self.sut.get_doc_html = mock.MagicMock(return_value=doc_html)
        result: LoadMangaResult = self.sut.load_manga('')
        self.assertIsInstance(result, LoadMangaResult)
        self.assertEqual(len(result.chapters), 235)
        self.assertEqual(result.author, 'Inagaki Riichiro')
        self.assertTrue(result.status)
        self.assertEqual(result.description, 'Durante 5 anos, Taiju Ooki tentou se confessar para o amor de sua vida, Yuzuriha, mas nunca conseguiu. Um dia ele decode reunir toda sua coragem para dizer a ela tudo o que sente... Mas EXATAMENTE nessa hora uma CATÁSTROFE de proporções globais extingue toda a humanidade transformando-a em pedra. Como únicos sobreviventes (até então) cabe a Taiju e seu brilhante amigo, o cientista Senkuu, fazerem a humanidade sair da Idade da Pedra, voltar a Era Moderna e salvar Yuzuriha.')


if __name__ == '__main__':
    unittest.main()