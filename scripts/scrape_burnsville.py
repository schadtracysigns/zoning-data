
import json
from playwright.sync_api import sync_playwright

def scrape_burnsville():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.burnsvillemn.gov/1900/Sign-Regulations")
        
        zoning_data = {
            "city": "Burnsville",
            "rules": []
        }

        elements = page.locator("div#content-wrapper *").all()
        for element in elements:
            text = element.inner_text().strip()
            if text:
                zoning_data["rules"].append(text)

        browser.close()

        with open("burnsville.json", "w") as f:
            json.dump(zoning_data, f, indent=2)

if __name__ == "__main__":
    scrape_burnsville()
