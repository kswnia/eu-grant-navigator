import requests
from bs4 import BeautifulSoup

def scrape_eu_page(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    sections = []
    current_section = "General"
    for tag in soup.find_all(['h1', 'h2', 'h3', 'p']):
        if tag.name in ['h1', 'h2', 'h3']:
            current_section = tag.get_text(strip=True)
        elif tag.name == 'p':
            content = tag.get_text(strip=True)
            if len(content) > 50:
                sections.append({
                    "section": current_section,
                    "source": url,
                    "content": content
                })
    return sections
