import json
import requests
import PyPDF2
import io

def download_and_parse_rochester_pdf():
    url = "https://www.rochestermn.gov/home/showpublisheddocument/32714/637489098228330000"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"❌ Failed to download PDF: Status {response.status_code}")

    reader = PyPDF2.PdfReader(io.BytesIO(response.content))
    full_text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            full_text += extracted + "\n"

    result = {
        "rochester": {
            "55901": {
                "General Sign Ordinance": {
                    "raw_text": full_text.strip()
                }
            }
        }
    }

    with open("rochester.json", "w") as f:
        json.dump(result, f, indent=2)

    # Update combined
    try:
        with open("zoning_combined.json", "r") as f:
            combined = json.load(f)
    except FileNotFoundError:
        combined = {}

    combined["rochester"] = result["rochester"]

    with open("zoning_combined.json", "w") as f:
        json.dump(combined, f, indent=2)

    print("✅ Rochester zoning data updated.")

if __name__ == "__main__":
    download_and_parse_rochester_pdf()
