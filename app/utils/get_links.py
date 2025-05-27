import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlsplit, urlunsplit


def normalize_url(url):
    parts = urlsplit(url)
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme, parts.netloc, path, "", ""))


def get_internal_links(base_url):
    try:
        r = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
    except Exception as e:
        print(f"Error fetching {base_url}: {e}")
        return []
    base_domain = urlparse(base_url).netloc.replace("www.", "")
    urls = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if not href or href.startswith(("#", "mailto:", "tel:")):
            continue
        url = urljoin(base_url, href)
        link_domain = urlparse(url).netloc.replace("www.", "")
        if link_domain != base_domain:
            continue
        norm_url = normalize_url(url)
        urls.add(norm_url)
    return list(urls)


def crawl_site(start_url, max_depth=2):
    visited = set()
    to_visit = [(start_url, 0)]
    all_internal = set()

    while to_visit:
        url, depth = to_visit.pop()
        if url in visited or depth > max_depth:
            continue
        visited.add(url)
        links = get_internal_links(url)
        all_internal.update(links)
        if depth < max_depth:
            for link in links:
                if link not in visited:
                    to_visit.append((link, depth + 1))
    return list(all_internal)
