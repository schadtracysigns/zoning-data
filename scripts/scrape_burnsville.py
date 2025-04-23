
# scripts/scrape_burnsville.py

import json

ZONES = ["Retail", "Commercial", "Residential"]
ZIP_CODE = "55306"

example_rules = {
    "max_height": "15 feet",
    "max_area": "100 sq ft",
    "illumination": "Internal and external allowed",
    "permit_required": "Yes"
}

def generate_zoning_data():
    return {
        "burnsville": {
            ZIP_CODE: {
                zone: example_rules.copy() for zone in ZONES
            }
        }
    }

def save_to_file(data, filename="burnsville.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    data = generate_zoning_data()
    save_to_file(data)
