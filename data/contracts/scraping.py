import urllib.request


class RequestPage:
    url = ''
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }

    def get_doc_html(self, route):
        url = '%s%s' % (self.url, route)
        req = urllib.request.Request(url=url, headers=self.header)
        doc_html = urllib.request.urlopen(req).read()
        return doc_html

