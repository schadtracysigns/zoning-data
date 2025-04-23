# scripts/scrape_burnsville.py

import requests
from bs4 import BeautifulSoup
import json
import time

URL = "https://burnsville.municipalcodeonline.com/book?type=ordinances#name=CHAPTER_10-30_SIGNS"
HEADERS = {"User-Agent": "Mozilla/5.0"}
SIGN_TYPES = ["Channel Letters", "Monument", "Pylon"]
ZONES = ["Retail", "Commercial", "Residential"]

def extract_sign_data():
    session = requests.Session()
    retries = 3
    success = False
    for attempt in range(retries):
        try:
            response = session.get(URL, headers=HEADERS, timeout=10)
            response.raise_for_status()
            success = True
            break
        except requests.RequestException as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(2)

    if not success:
        print("Failed to retrieve Burnsville signage data after several attempts.")
        return {}

    soup = BeautifulSoup(response.content, "html.parser")
    content_div = soup.find("div", class_="document-viewer__container")
    paragraphs = content_div.find_all("p") if content_div else []

    zone_data = {zone: {} for zone in ZONES}

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

    for zone in zone_data:
        for sign in zone_data[zone]:
            zone_data[zone][sign] = {"Raw Text": "\n".join(zone_data[zone][sign])}

    return {"burnsville": {"55306": zone_data}}

def save_json(data, filename="burnsville.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    data = extract_sign_data()
    if data:
        save_json(data)
    else:
        print("No data extracted.")
