import json
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def scrape_burnsville_signs():
    url = "https://burnsville.municipalcodeonline.com/book?type=ordinances#name=CHAPTER_10-30_SIGNS"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        # Wait 10 seconds to ensure ordinance content is loaded
        page.wait_for_timeout(10000)

        html = page.content()
        soup = BeautifulSoup(html, "html.parser")

        zoning_data = {}
        sections = soup.find_all("div", class_="section")

        for section in sections:
            h3 = section.find("h3")
            if h3:
                title = h3.get_text(strip=True)
                content = section.get_text(separator="\n", strip=True)
                if not any(x in content for x in ["Session Timeout", "Document Creator", "Votes"]):
                    zoning_data[title] = content

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

        print("✅ Burnsville zoning data saved.")

        browser.close()

if __name__ == "__main__":
    scrape_burnsville_signs()
