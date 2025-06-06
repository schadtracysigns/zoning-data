import json

def scrape_burnsville():
    zoning_data = {
        "city": "Burnsville",
        "zoning_link": "https://www.burnsvillemn.gov/1900/Sign-Regulations",
        "zones": {
            "Commercial": {
                "Pylon": {
                    "max_height": "30 feet",
                    "max_area": "100 sq ft per face",
                    "illumination": "Internal or external allowed",
                    "permit_required": "Yes",
                    "letter_depth": "Optional",
                    "cabinet_signs_allowed": "Allowed",
                    "painted_signs": "Not allowed",
                    "location_restriction": "Only one per parcel unless variance approved"
                },
                "Channel Letters": {
                    "max_height": "24 inches",
                    "max_area": "10% of wall face",
                    "illumination": "Internal allowed",
                    "permit_required": "Yes",
                    "letter_depth": "3 inches minimum",
                    "cabinet_signs_allowed": "No",
                    "painted_signs": "Not allowed",
                    "location_restriction": "Must be attached to primary building face"
                },
                "Monument": {
                    "max_height": "6 feet",
                    "max_area": "60 sq ft",
                    "illumination": "External only",
                    "permit_required": "Yes",
                    "letter_depth": "Optional",
                    "cabinet_signs_allowed": "Yes",
                    "painted_signs": "No",
                    "location_restriction": "Front yard setback required"
                },
                "Vinyl": {
                    "max_height": "N/A",
                    "max_area": "20% of window area",
                    "illumination": "N/A",
                    "permit_required": "No",
                    "letter_depth": "N/A",
                    "cabinet_signs_allowed": "N/A",
                    "painted_signs": "Allowed",
                    "location_restriction": "Interior window application only"
                }
            },
            "Residential": {
                "Pylon": {
                    "max_height": "10 feet",
                    "max_area": "32 sq ft",
                    "illumination": "Not allowed",
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
                    "max_height": "5 feet",
                    "max_area": "40 sq ft",
                    "illumination": "External allowed",
                    "permit_required": "Yes",
                    "letter_depth": "Optional",
                    "cabinet_signs_allowed": "Yes",
                    "painted_signs": "Allowed",
                    "location_restriction": "Must meet residential setback requirements"
                },
                "Vinyl": {
                    "max_height": "N/A",
                    "max_area": "15% of window area",
                    "illumination": "N/A",
                    "permit_required": "No",
                    "letter_depth": "N/A",
                    "cabinet_signs_allowed": "N/A",
                    "painted_signs": "Allowed",
                    "location_restriction": "Interior window application only"
                }
            },
            "Downtown": {
                "Pylon": {
                    "max_height": "20 feet",
                    "max_area": "50 sq ft",
                    "illumination": "Internal allowed",
                    "permit_required": "Yes",
                    "letter_depth": "Optional",
                    "cabinet_signs_allowed": "Allowed",
                    "painted_signs": "No",
                    "location_restriction": "Pedestrian scale encouraged"
                },
                "Channel Letters": {
                    "max_height": "30 inches",
                    "max_area": "15% of wall face",
                    "illumination": "Internal allowed",
                    "permit_required": "Yes",
                    "letter_depth": "3 inches minimum",
                    "cabinet_signs_allowed": "No",
                    "painted_signs": "Not allowed",
                    "location_restriction": "Attached to building facade"
                },
                "Monument": {
                    "max_height": "6 feet",
                    "max_area": "40 sq ft",
                    "illumination": "External or Internal allowed",
                    "permit_required": "Yes",
                    "letter_depth": "Optional",
                    "cabinet_signs_allowed": "Yes",
                    "painted_signs": "Allowed",
                    "location_restriction": "Street-facing orientation required"
                },
                "Vinyl": {
                    "max_height": "N/A",
                    "max_area": "25% of window area",
                    "illumination": "N/A",
                    "permit_required": "No",
                    "letter_depth": "N/A",
                    "cabinet_signs_allowed": "N/A",
                    "painted_signs": "Allowed",
                    "location_restriction": "Interior window application only"
                }
            }
        }
    }

    with open("burnsville.json", "w") as f:
        json.dump(zoning_data, f, indent=2)

if __name__ == "__main__":
    scrape_burnsville()
