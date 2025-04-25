import json
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def scrape_burnsville_signs():
    url = "https://burnsville.municipalcodeonline.com/book?type=ordinances#name=CHAPTER_10-30_SIGNS"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(8000)  # Give it time to load full dynamic JS

        html = page.content()
        soup = BeautifulSoup(html, "html.parser")

        zoning_data = {}
        section_container = soup.find("div", class_="reader-container")
        if section_container:
            for div in section_container.find_all("div", recursive=False):
                header = div.find("h3")
                body = div.get_text(separator="\n", strip=True)
                if header:
                    heading = header.get_text(strip=True)
                    zoning_data[heading] = body

        result = {
            "burnsville": {
                "55306": {
                    "General Sign Ordinance": zoning_data
                }
            }
        }

        with open("burnsville.json", "w") as f:
            json.dump(result, f, indent=2)

        try:
            with open("zoning_combined.json", "r") as f:
                combined = json.load(f)
        except FileNotFoundError:
            combined = {}

        combined["burnsville"] = result["burnsville"]

        with open("zoning_combined.json", "w") as f:
            json.dump(combined, f, indent=2)

        print("✅ Burnsville zoning data updated.")
        browser.close()

if __name__ == "__main__":
    scrape_burnsville_signs()
