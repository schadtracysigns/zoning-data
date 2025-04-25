import json
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def scrape_burnsville_signs():
    url = "https://burnsville.municipalcodeonline.com/book?type=ordinances#name=CHAPTER_10-30_SIGNS"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(5000)

        # Extract dynamic HTML content
        soup = BeautifulSoup(page.content(), "html.parser")

        sections = soup.find_all("div", class_="section")
        zoning_data = {}

        for section in sections:
            header = section.find("h3")
            if header:
                title = header.get_text(strip=True)
                content = section.get_text(separator="\n", strip=True)
                zoning_data[title] = content

        formatted = {
            "burnsville": {
                "55306": {
                    "General Sign Ordinance": zoning_data
                }
            }
        }

        with open("burnsville.json", "w") as f:
            json.dump(formatted, f, indent=2)

        try:
            with open("zoning_combined.json", "r") as f:
                combined = json.load(f)
        except FileNotFoundError:
            combined = {}

        combined["burnsville"] = formatted["burnsville"]

        with open("zoning_combined.json", "w") as f:
            json.dump(combined, f, indent=2)

        print("✅ Burnsville zoning updated.")

        browser.close()

if __name__ == "__main__":
    scrape_burnsville_signs()
