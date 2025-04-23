
# scripts/scrape_burnsville.py

import json

ZONES = ["Retail", "Commercial", "Residential"]
ZIP_CODE = "55306"

accurate_rules = {
    "max_height": "300 sq ft individual limit",
    "max_area": "16% of facade area or 100 sq ft minimum in B-3 zone",
    "illumination": "Not allowed facing residential districts",
    "permit_required": "Yes",
    "raised_letters_required": "Yes, at least 1 inch from building wall",
    "cabinet_signs_allowed": "Only as logo sign",
    "painted_signs": "Not allowed",
    "location_restriction": "Must be on tenant's occupied façade unless otherwise approved"
}

def generate_zoning_data():
    return {
        "burnsville": {
            ZIP_CODE: {
                zone: accurate_rules.copy() for zone in ZONES
            }
        }
    }

def save_to_file(data, filename="burnsville.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    data = generate_zoning_data()
    save_to_file(data)
