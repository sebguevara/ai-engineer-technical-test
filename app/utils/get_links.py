import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlsplit, urlunsplit

def normalize_url(url):
    parts = urlsplit(url)
    path = parts.path.rstrip('/') or '/'
    return urlunsplit((parts.scheme, parts.netloc, path, '', ''))

def get_internal_links(base_url):
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "html.parser")
    base_domain = urlparse(base_url).netloc.replace('www.', '')
    urls = set()
    for a in soup.find_all('a', href=True):
        href = a['href']
        if not href or href.startswith(('#', 'mailto:', 'tel:')):
            continue
        url = urljoin(base_url, href)
        link_domain = urlparse(url).netloc.replace('www.', '')
        if link_domain != base_domain: 
            continue
        norm_url = normalize_url(url)
        urls.add(norm_url)
    return list(urls)