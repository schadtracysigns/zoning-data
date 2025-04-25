import json
from playwright.sync_api import sync_playwright

def scrape_burnsville_signs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://burnsville.municipalcodeonline.com/book?type=ordinances#name=CHAPTER_10-30_SIGNS")

        # Wait up to 15s for visible ordinance content
        page.wait_for_selector("div.section h3", timeout=15000)

        # Extract data directly from visible page elements
        titles = page.locator("div.section h3").all_inner_texts()
        bodies = page.locator("div.section").all_inner_texts()

        zoning_data = {}
        for i in range(len(titles)):
            heading = titles[i].strip()
            body = bodies[i].strip()
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

        print("✅ LIVE ordinance data pulled successfully.")

        browser.close()

if __name__ == "__main__":
    scrape_burnsville_signs()
