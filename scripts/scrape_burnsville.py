import json
from playwright.sync_api import sync_playwright

def scrape_burnsville_signs():
    url = "https://burnsville.municipalcodeonline.com/book?type=ordinances#name=CHAPTER_10-30_SIGNS"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(8000)  # Wait for JavaScript to render fully

        # Use Playwright's DOM traversal instead of BeautifulSoup
        sections = page.locator("div.section")
        count = sections.count()

        zoning_data = {}

        for i in range(count):
            section = sections.nth(i)
            try:
                title = section.locator("h3").inner_text()
                content = section.inner_text()
                zoning_data[title.strip()] = content.strip()
            except:
                continue

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

        print("✅ Burnsville data scraped from live page.")

        browser.close()

if __name__ == "__main__":
    scrape_burnsville_signs()
