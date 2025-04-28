
import json
from playwright.sync_api import sync_playwright

def scrape_rochester():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.rochestermn.gov/government/departments/community-development/sign-regulations")
        
        zoning_data = {
            "city": "Rochester",
            "rules": []
        }

        elements = page.locator("div#content-wrapper *").all()
        for element in elements:
            text = element.inner_text().strip()
            if text:
                zoning_data["rules"].append(text)

        browser.close()

        with open("rochester.json", "w") as f:
            json.dump(zoning_data, f, indent=2)

if __name__ == "__main__":
    scrape_rochester()
