# scripts/scrape_burnsville.py

import requests
from bs4 import BeautifulSoup
import json

URL = "https://burnsville.municipalcodeonline.com/book?type=ordinances#name=CHAPTER_10-30_SIGNS"
HEADERS = {"User-Agent": "Mozilla/5.0"}

SIGN_TYPES = ["Channel Letters", "Monument", "Pylon"]
ZONES = ["Retail", "Commercial", "Residential"]


def extract_sign_data():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")

    content_div = soup.find("div", class_="document-viewer__container")
    paragraphs = content_div.find_all("p") if content_div else []

    zone_data = {
        "Retail": {},
        "Commercial": {},
        "Residential": {}
    }

    current_zone = None
    current_sign_type = None

    for p in paragraphs:
        text = p.get_text(strip=True)

        for zone in ZONES:
            if zone.lower() in text.lower():
                current_zone = zone
                current_sign_type = None

        for sign in SIGN_TYPES:
            if sign.lower() in text.lower():
                current_sign_type = sign
                if current_zone:
                    zone_data[current_zone][current_sign_type] = []

        if current_zone and current_sign_type:
            zone_data[current_zone][current_sign_type].append(text)

    # Convert list entries to readable joined strings
    for zone in zone_data:
        for sign in zone_data[zone]:
            zone_data[zone][sign] = {"Raw Text": "\n".join(zone_data[zone][sign])}

    data = {
        "burnsville": {
            "55306": zone_data
        }
    }

    return data


def save_json(data, filename="burnsville.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    zoning_data = extract_sign_data()
    save_json(zoning_data)
