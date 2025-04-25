import json
from playwright.sync_api import sync_playwright

def scrape_burnsville_signs():
    url = "https://burnsville.municipalcodeonline.com/book?type=ordinances#name=CHAPTER_10-30_SIGNS"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(10000)  # Give JavaScript time to inject content

        # Use Playwright locator system to read what’s on screen
        sections = page.locator("div.section")
        count = sections.count()

        zoning_data = {}

        for i in range(count):
            try:
                section = sections.nth(i)
                heading = section.locator("h3").inner_text()
                body = section.inner_text()
                zoning_data[heading.strip()] = body.strip()
            except:
                continue

        output = {
            "burnsville": {
                "55306": {
                    "General Sign Ordinance": zoning_data
                }
            }
        }

        with open("burnsville.json", "w") as f:
            json.dump(output, f, indent=2)

        try:
            with open("zoning_combined.json", "r") as f:
                combined = json.load(f)
        except FileNotFoundError:
            combined = {}

        combined["burnsville"] = output["burnsville"]

        with open("zoning_combined.json", "w") as f:
            json.dump(combined, f, indent=2)

        print("✅ Zoning data extracted from Burnsville site.")
        browser.close()

if __name__ == "__main__":
    scrape_burnsville_signs()
