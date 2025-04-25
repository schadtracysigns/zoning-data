import json
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def scrape_burnsville_signs():
    url = "https://burnsville.municipalcodeonline.com/book?type=ordinances#name=CHAPTER_10-30_SIGNS"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        # Wait for JS content to fully render
        page.wait_for_timeout(10000)

        html = page.content()
        soup = BeautifulSoup(html, "html.parser")

        zoning_data = {}
        sections = soup.find_all("div", class_="section")

        for section in sections:
            h3 = section.find("h3")
            if h3:
                heading = h3.get_text(strip=True)
                content = section.get_text(separator="\n", strip=True)
                zoning_data[heading] = content

        burnsville_data = {
            "burnsville": {
                "55306": {
                    "General Sign Ordinance": zoning_data
                }
            }
        }

        # Write to burnsville.json
        with open("burnsville.json", "w") as f:
            json.dump(burnsville_data, f, indent=2)

        # Merge with combined zoning data
        try:
            with open("zoning_combined.json", "r") as f:
                combined = json.load(f)
        except FileNotFoundError:
            combined = {}

        combined["burnsville"] = burnsville_data["burnsville"]

        with open("zoning_combined.json", "w") as f:
            json.dump(combined, f, indent=2)

        print("✅ LIVE Burnsville data pulled and saved.")

        browser.close()

if __name__ == "__main__":
    scrape_burnsville_signs()
