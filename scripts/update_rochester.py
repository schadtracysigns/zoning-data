import json
import fitz  # PyMuPDF
import requests

PDF_URL = "https://www.rochestermn.gov/home/showpublisheddocument/36333/638695059544470000"
PDF_PATH = "roch_udc.pdf"
JSON_PATH = "rochester.json"

def download_rochester_pdf():
    print("📥 Downloading Rochester sign code PDF...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(PDF_URL, headers=headers)
    response.raise_for_status()
    with open(PDF_PATH, "wb") as f:
        f.write(response.content)


def extract_signage_data(pdf_path):
    doc = fitz.open(pdf_path)
    text = "".join(page.get_text() for page in doc)

    # Simulated data; replace with real parsed logic
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
    download_rochester_pdf()
    data = extract_signage_data(PDF_PATH)
    with open(JSON_PATH, "w") as f:
        json.dump(data, f, indent=2)
    print("✅ Rochester zoning data saved.")
