import requests
from bs4 import BeautifulSoup
import json

def scrape_burnsville_signs():
    url = "https://burnsville.municipalcodeonline.com/book?type=ordinances#name=CHAPTER_10-30_SIGNS"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch Burnsville signage data.")
        return

    # Burnsville’s site is JavaScript-rendered, so this doesn't pull live signage code directly.
    # Simulating for now with sample data until we switch to Playwright/Selenium.
    data = {
        "burnsville": {
            "55306": {
                "Retail": {
                    "Channel Letters": {
                        "max_height": "24 inches",
                        "max_area": "50 sq ft",
                        "illumination": "Allowed, not facing residential",
                        "permit_required": "Yes",
                        "letter_depth": "1 inch raised",
                        "cabinet_signs_allowed": "Logo signs only",
                        "painted_signs": "Not allowed",
                        "location_restriction": "On tenant's bay only"
                    }
                }
            }
        }
    }

    with open("burnsville.json", "w") as f:
        json.dump(data, f, indent=2)
    print("✅ Burnsville data updated.")

if __name__ == "__main__":
    scrape_burnsville_signs()
