from data.contracts.search_manga_repository import SearchMangaRepository
from data.contracts.load_manga_repository import LoadMangaRepository
from data.contracts.load_chapter_repository import LoadChapterRepository
from data.models.manga import MangaModel, ChapterModel, PageModel
from bs4 import BeautifulSoup
from data.contracts.scraping import RequestPage


class MangaHostRepository(SearchMangaRepository, LoadMangaRepository, LoadChapterRepository, RequestPage):
    url = 'https://mangahosted.com/'

    def search_manga(self, name: str) -> list[MangaModel]:
        route = 'find/%s' % (name.replace(' ', '+'))
        doc_html = self.get_doc_html(route)
        soup = BeautifulSoup(doc_html, 'html.parser')
        tag_tr_list = soup.find('table', class_ ='table table-search table-hover').tbody.find_all('tr') # type: ignore
        manga_list = []
        for tag_result in tag_tr_list:
            find = tag_result.find('a', class_='pull-left')
            tag_a = find
            desc = tag_result.find('div', class_='entry-content').text
            # sub = tag_result.find('span', class_='muted').text
            title = tag_a['title']
            path = tag_a['href']

            manga = MangaModel(title, path)
            manga.description = desc
            manga.picture = tag_a.picture.source['srcset']
            manga_list.append(manga)
        return manga_list

    def load_manga(self, identifier: str) -> MangaModel:
        doc_html = self.get_doc_html(identifier)
        soup = BeautifulSoup(doc_html, 'html.parser')
        base_tag = soup.find('article', class_='ejeCg')
        name = base_tag.find('h1', class_='title').text # type: ignore
        chapters_tag_div = base_tag.find('div', class_='chapters').find_all('div', class_='cap')# type: ignore
        
        load_manga_result = MangaModel(name=name, path=identifier)
        load_manga_result.set_chapter([ChapterModel(
            manga=load_manga_result,
            title=chapter_tag.find('a', class_='btn-caps w-button').text,
            number=float(chapter_tag.find('a', class_='btn-caps w-button').text), # type: ignore
            path=chapter_tag.find('a', class_='btn-green w-button pull-left')['href']
            ) for chapter_tag in chapters_tag_div])
        load_manga_result.description = base_tag.find('div', class_='paragraph').find('p').text # type: ignore
        load_manga_result.author = base_tag.find('ul', class_='w-list-unstyled').find_all('div')[2].contents[1] # type: ignore
        load_manga_result.status = base_tag.find('ul', class_='w-list-unstyled').find_all('div')[1].contents[1] # type: ignore
        return load_manga_result
    
    def load_chapter(self, identifier) -> ChapterModel:
        doc_html = self.get_doc_html(identifier)
        soup = BeautifulSoup(doc_html, 'html.parser')
        base_tag = soup.find(id='slider')
        page_list = [PageModel(
            chapter=None, 
            index=int(a_tag['data-read-hash']),
            path=a_tag.find('img')['src']) for a_tag in base_tag.find_all('a')]
        chapter = ChapterModel(manga=None, number=1, title='', path='')
        chapter.set_pages(page=page_list)
        return chapter