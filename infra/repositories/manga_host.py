from data.contracts.load_manga_repository import LoadMangaRepository
from data.models.manga import LoadMangaResult
from bs4 import BeautifulSoup
from data.contracts.scraping import RequestPage

class MangaHostRepository(LoadMangaRepository, RequestPage):
    url = 'https://mangahosted.com/'

    def load_manga(self, name: str, **kwargs) -> list[LoadMangaResult]:
        self.url = '%sfind/%s' % (self.url, name.replace(' ', '+'))
        doc_html = self.get_doc_html()
        soup = BeautifulSoup(doc_html, 'html.parser')
        tag_tr_list = soup.find('table', class_='table table-search table-hover').tbody.find_all('tr')
        manga_list = []
        for tag_result in tag_tr_list:
            find = tag_result.find('a', class_='pull-left')
            tag_a = find
            describe = tag_tr_list[0].find('div', class_='entry-content').text
            manga = LoadMangaResult(tag_a['title'], tag_a['href'])
            manga.picture = tag_a.picture.source['srcset']
            manga_list.append(manga)
        return manga_list

