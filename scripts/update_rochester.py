import json
import requests
import PyPDF2
import io

def download_and_parse_rochester_pdf():
    pdf_url = "https://www.rochestermn.gov/home/showpublisheddocument/32714/637489098228330000"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(pdf_url, headers=headers)

    if response.status_code != 200:
        raise Exception("Failed to download Rochester PDF.")

    reader = PyPDF2.PdfReader(io.BytesIO(response.content))
    full_text = ""

    for page in reader.pages:
        full_text += page.extract_text() + "\n"

    rochester_data = {
        "rochester": {
            "55901": {
                "General Sign Ordinance": {
                    "raw_text": full_text.strip()
                }
            }
        }
    }

    with open("rochester.json", "w") as f:
        json.dump(rochester_data, f, indent=2)

    try:
        with open("zoning_combined.json", "r") as f:
            combined = json.load(f)
    except FileNotFoundError:
        combined = {}

    combined["rochester"] = rochester_data["rochester"]

    with open("zoning_combined.json", "w") as f:
        json.dump(combined, f, indent=2)

    print("✅ Rochester zoning updated.")

if __name__ == "__main__":
    download_and_parse_rochester_pdf()
