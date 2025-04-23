import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = "https://burnsville.municipalcodeonline.com/book?type=ordinances#name=CHAPTER_10-30_SIGNS"
html_url = "https://burnsville.municipalcodeonline.com/book?type=ordinances&name=CHAPTER_10-30_SIGNS"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Request ordinance page HTML (not JS version)
response = requests.get(html_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Look for content blocks or paragraphs
sections = soup.select("div.content") or soup.find_all("p")
text_blocks = []

for section in sections:
    for p in section.find_all("p"):
        if p.text.strip():
            text_blocks.append(p.text.strip())

# Generate simplified JSON structure
burnsville_json = {
    "burnsville": {
        "55306": {
            "General": {
                "FullText": text_blocks,
                "Source": url,
                "LastUpdated": str(datetime.now().date())
            }
        }
    }
}

# Write output
with open("burnsville.json", "w") as f:
    json.dump(burnsville_json, f, indent=2)
