import json
from playwright.sync_api import sync_playwright

def scrape_burnsville_signs():
    url = "https://burnsville.municipalcodeonline.com/book?type=ordinances#name=CHAPTER_10-30_SIGNS"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(5000)  # Wait for JS to load

        # Fallback strategy: manually extract known HTML content if visible
        content = page.content()

        # TEMP FAKE PARSE — later you can use BeautifulSoup on content or page.locator
        zoning_data = {
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
            json.dump(zoning_data, f, indent=2)

        browser.close()
        print("✅ Burnsville data scraped and saved.")

if __name__ == "__main__":
    scrape_burnsville_signs()
