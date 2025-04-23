import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = "https://burnsville.municipalcodeonline.com/book?type=ordinances&name=CHAPTER_10-30_SIGNS"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

content_div = soup.find("div", class_="content")
paragraphs = []

if content_div:
    for p in content_div.find_all("p"):
        text = p.get_text(strip=True)
        if text:
            paragraphs.append(text)

# Save in JSON structure compatible with your app
burnsville_data = {
    "burnsville": {
        "55306": {
            "General": {
                "FullText": paragraphs,
                "Source": url,
                "LastUpdated": str(datetime.now().date())
            }
        }
    }
}

with open("burnsville.json", "w") as f:
    json.dump(burnsville_data, f, indent=2)
