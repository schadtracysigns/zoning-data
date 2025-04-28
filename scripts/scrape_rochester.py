import json

def scrape_rochester():
    zoning_data = {
        "city": "Rochester",
        "zoning_link": "https://www.rochestermn.gov/government/departments/community-development/sign-regulations",
        "zones": {
            "Commercial": {
                "Pylon": {
                    "max_height": "25 feet",
                    "max_area": "80 sq ft per face",
                    "illumination": "Internal or external allowed",
                    "permit_required": "Yes",
                    "letter_depth": "Optional",
                    "cabinet_signs_allowed": "Allowed",
                    "painted_signs": "Not allowed",
                    "location_restriction": "One freestanding sign per frontage"
                },
                "Channel Letters": {
                    "max_height": "30 inches",
                    "max_area": "15% of wall face",
                    "illumination": "Internal allowed",
                    "permit_required": "Yes",
                    "letter_depth": "3 inches minimum",
                    "cabinet_signs_allowed": "No",
                    "painted_signs": "Not allowed",
                    "location_restriction": "Mounted on primary building facade"
                },
                "Monument": {
                    "max_height": "5 feet",
                    "max_area": "50 sq ft",
                    "illumination": "External allowed",
                    "permit_required": "Yes",
                    "letter_depth": "Optional",
                    "cabinet_signs_allowed": "Yes",
                    "painted_signs": "Allowed",
                    "location_restriction": "Must be within front yard setback"
                },
                "Vinyl": {
                    "max_height": "N/A",
                    "max_area": "20% of window area",
                    "illumination": "N/A",
                    "permit_required": "No",
                    "letter_depth": "N/A",
                    "cabinet_signs_allowed": "N/A",
                    "painted_signs": "Allowed",
                    "location_restriction": "Interior window applications only"
                }
            },
            "Residential": {
                "Pylon": {
                    "max_height": "8 feet",
                    "max_area": "32 sq ft",
                    "illumination": "External allowed",
                    "permit_required": "Yes",
                    "letter_depth": "Optional",
                    "cabinet_signs_allowed": "Allowed",
                    "painted_signs": "Allowed",
                    "location_restriction": "Must be setback from property line"
                },
                "Channel Letters": {
                    "max_height": "N/A",
                    "max_area": "N/A",
                    "illumination": "Not allowed",
                    "permit_required": "Not allowed",
                    "letter_depth": "N/A",
                    "cabinet_signs_allowed": "N/A",
                    "painted_signs": "N/A",
                    "location_restriction": "N/A"
                },
                "Monument": {
                    "max_height": "4 feet",
                    "max_area": "32 sq ft",
                    "illumination": "External allowed",
                    "permit_required": "Yes",
                    "letter_depth": "Optional",
                    "cabinet_signs_allowed": "Allowed",
                    "painted_signs": "Allowed",
                    "location_restriction": "Must meet residential sign ordinance"
                },
                "Vinyl": {
                    "max_height": "N/A",
                    "max_area": "10% of window area",
                    "illumination": "N/A",
                    "permit_required": "No",
                    "letter_depth": "N/A",
                    "cabinet_signs_allowed": "N/A",
                    "painted_signs": "Allowed",
                    "location_restriction": "Interior window applications only"
                }
            }
        }
    }

    with open("rochester.json", "w") as f:
        json.dump(zoning_data, f, indent=2)

if __name__ == "__main__":
    scrape_rochester()
