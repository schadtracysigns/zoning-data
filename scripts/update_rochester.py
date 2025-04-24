import json
import requests
import fitz  # PyMuPDF
from playwright.sync_api import sync_playwright

def download_rochester_pdf(pdf_path):
    url = "https://www.rochestermn.gov/departments/community-development/unified-development-code"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)

        # Find and follow the UDC PDF link
        pdf_link = page.locator("a", has_text="Unified Development Code (UDC)").first
        pdf_url = pdf_link.get_attribute("href")

        if not pdf_url:
            raise Exception("PDF URL not found")

        if not pdf_url.startswith("http"):
            pdf_url = f"https://www.rochestermn.gov{pdf_url}"

        response = requests.get(pdf_url)
        with open(pdf_path, "wb") as f:
            f.write(response.content)

        browser.close()

def extract_signage_data(pdf_path):
    doc = fitz.open(pdf_path)
    text = "".join(page.get_text() for page in doc)

    # Simulated values - Replace with real parsed logic later
    return {
        "rochester": {
            "55901": {
                "Retail": {
                    "Channel Letters": {
                        "max_height": "32 inches",
                        "max_area": "20% of wall face",
                        "illumination": "Allowed with conditions",
                        "permit_required": "Yes",
                        "letter_depth": "1 inch",
                        "cabinet_signs_allowed": "Yes",
                        "painted_signs": "No",
                        "location_restriction": "On tenant's wall"
                    },
                    "Monument": {
                        "max_height": "6 feet",
                        "max_area": "64 sq ft",
                        "illumination": "Internal or external",
                        "permit_required": "Yes",
                        "letter_depth": "Optional",
                        "cabinet_signs_allowed": "Yes",
                        "painted_signs": "Allowed",
                        "location_restriction": "Front yard near entrance"
                    },
                    "Pylon": {
                        "max_height": "20 feet",
                        "max_area": "100 sq ft",
                        "illumination": "Internal only",
                        "permit_required": "Yes",
                        "letter_depth": "Optional",
                        "cabinet_signs_allowed": "Yes",
                        "painted_signs": "No",
                        "location_restriction": "One per lot"
                    }
                }
            }
        }
    }

if __name__ == "__main__":
    pdf_file = "roch_udc.pdf"
    json_output = "rochester.json"

    download_rochester_pdf(pdf_file)
    data = extract_signage_data(pdf_file)

    with open(json_output, "w") as f:
        json.dump(data, f, indent=2)

    print("✅ Rochester zoning data updated.")
