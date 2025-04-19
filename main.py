import requests
from bs4 import BeautifulSoup
import json


import time





def scrape_eu_page(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    sections = []
    current_section = "General"

    # Traverse through tags in order to maintain context
    for tag in soup.find_all(['h1', 'h2', 'h3', 'p']):
        if tag.name in ['h1', 'h2', 'h3']:
            current_section = tag.get_text(strip=True)
        elif tag.name == 'p':
            content = tag.get_text(strip=True)
            if len(content) > 50:  # Avoid short/noise content
                sections.append({
                    "section": current_section,
                    "source": url,
                    "content": content
                })

    return sections




# 🚀 Replace with the EU grants page you're scraping
url = 'https://commission.europa.eu/funding-tenders/find-funding/eu-funding-programmes_en'

# Run scraper
data = scrape_eu_page(url)

# ✅ Save to JSON file
with open("eu_grants_structured.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# 🔎 Quick preview
print(f"Extracted {len(data)} sections. Sample:")
for d in data[:3]:
    print(f"\n[{d['section']}]\n{d['content'][:200]}...\n")
