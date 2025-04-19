import json
import time
import os
import re

def sanitize_filename(url):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', url[-50:])[:50]

def save_json_with_timestamp(data, folder="data/processed_chunks"):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"eu_grants_{timestamp}.json"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved data to {path}")
