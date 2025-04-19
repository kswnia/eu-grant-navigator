import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

visited = set()

def is_valid_link(href, base_url):
    if not href:
        return False
    if href.startswith("#") or "javascript:" in href:
        return False
    full_url = urljoin(base_url, href)
    domain = urlparse(base_url).netloc
    return domain in full_url and "funding" in full_url.lower()

def get_all_grant_links(base_url, limit=20):
    to_visit = [base_url]
    found_links = []
    while to_visit and len(found_links) < limit:
        current_url = to_visit.pop(0)
        if current_url in visited:
            continue
        visited.add(current_url)
        try:
            response = requests.get(current_url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            links = [urljoin(current_url, a['href']) for a in soup.find_all('a', href=True)
                     if is_valid_link(a['href'], base_url)]
            for link in links:
                if link not in visited and link not in to_visit:
                    to_visit.append(link)
                    found_links.append(link)
        except Exception as e:
            print(f"Failed to fetch {current_url}: {e}")
        time.sleep(1)
    return list(set(found_links))
