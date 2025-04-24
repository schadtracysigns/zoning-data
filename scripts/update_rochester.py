import json

# Simulated scraped zoning data (replace with real logic later)
data = {
    "rochester": {
        "55901": {
            "Commercial": {
                "Advertising Sign": {
                    "max_height": "30 feet",
                    "max_area": "100 sq ft",
                    "illumination": "Allowed with zoning restrictions",
                    "permit_required": "Yes",
                    "setback_requirements": "20 feet from ROW",
                    "proximity_restrictions": "Not within 300 ft of schools, churches",
                    "residential_buffer": "Not within 100 ft of residential zones"
                }
            }
        }
    }
}

with open("rochester.json", "w") as f:
    json.dump(data, f, indent=2)
