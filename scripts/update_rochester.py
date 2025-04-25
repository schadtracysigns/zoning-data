import json
import requests
import PyPDF2
import io
import re

def download_and_parse_rochester_pdf():
    pdf_url = "https://www.rochestermn.gov/home/showpublisheddocument/32714/637489098228330000"
    response = requests.get(pdf_url)

    if response.status_code != 200:
        raise Exception("Failed to download Rochester PDF.")

    reader = PyPDF2.PdfReader(io.BytesIO(response.content))
    full_text = ""

    for page in reader.pages:
        full_text += page.extract_text() + "\n"

    # Basic formatting (you can add more parsing here)
    rochester_data = {
        "rochester": {
            "55902": {
                "General Sign Ordinance": {
                    "raw_text": full_text.strip()
                }
            }
        }
    }

    # Save to rochester.json
    with open("rochester.json", "w") as f:
        json.dump(rochester_data, f, indent=2)

    # Merge into zoning_combined.json
    try:
        with open("zoning_combined.json", "r") as f:
            combined = json.load(f)
    except FileNotFoundError:
        combined = {}

    combined["rochester"] = rochester_data["rochester"]

    with open("zoning_combined.json", "w") as f:
        json.dump(combined, f, indent=2)

    print("✅ Rochester zoning data scraped and combined successfully.")

if __name__ == "__main__":
    download_and_parse_rochester_pdf()
