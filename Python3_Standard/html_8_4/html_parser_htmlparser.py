# -*- coding:utf-8 -*-
from html.parser import HTMLParser


def get_links(html):
    class URLSeeker(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.urls = []

        def handle_starttag(self, tag, attrs):
            href = dict(attrs).get("href")
            if href and tag == "link":
                self.urls.append(href)

    url_seeker = URLSeeker()
    url_seeker.feed(html)
    return url_seeker.urls


if __name__ == '__main__':
    import requests
    from urllib.parse import urljoin

    base_url = 'http://www.baidu.com'
    url = '/s?wd=aaa'
    url_a = urljoin(base_url, url)
    res = requests.get(url_a)
    print(get_links(res.text))
