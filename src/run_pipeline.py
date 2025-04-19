from crawler import get_all_grant_links
from scrapper import scrape_eu_page
from processor import clean_chunks
from save_utils import save_json_with_timestamp
from config import BASE_URL, CRAWL_LIMIT

def run():
    links = get_all_grant_links(BASE_URL, limit=CRAWL_LIMIT)
    all_chunks = []
    for url in links:
        print(f"Scraping {url}")
        try:
            sections = scrape_eu_page(url)
            cleaned = clean_chunks(sections)
            all_chunks.extend(cleaned)
        except Exception as e:
            print(f"Error scraping {url}: {e}")
    save_json_with_timestamp(all_chunks)

if __name__ == "__main__":
    run()
