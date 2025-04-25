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

        # Grab the raw HTML
        content = page.content()
        soup = BeautifulSoup(content, "html.parser")

        # Try to find the ordinance section text
        sections = soup.find_all("div", class_="section")  # or adjust if needed
        burnsville_data = {}

        for section in sections:
            header = section.find("h3")
            if header:
                heading = header.get_text(strip=True)
                body = section.get_text(separator="\n", strip=True)

                burnsville_data[heading] = body

        # Format for app
        zoning_output = {
            "burnsville": {
                "55306": {
                    "General Sign Ordinance": burnsville_data
                }
            }
        }

        # Save to burnsville.json
        with open("burnsville.json", "w") as f:
            json.dump(zoning_output, f, indent=2)

        # Merge with zoning_combined.json
        try:
            with open("zoning_combined.json", "r") as f:
                combined = json.load(f)
        except FileNotFoundError:
            combined = {}

        combined["burnsville"] = zoning_output["burnsville"]

        with open("zoning_combined.json", "w") as f:
            json.dump(combined, f, indent=2)

        print("✅ Burnsville zoning data scraped and combined successfully.")

        browser.close()

if __name__ == "__main__":
    scrape_burnsville_signs()
