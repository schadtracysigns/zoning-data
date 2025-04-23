import json
from datetime import datetime

burnsville_data = {
    "burnsville": {
        "55306": {
            "Retail": {
                "Channel Letters": {
                    "Max Height": "24 in",
                    "Max Width": "96 in",
                    "Illumination": "Internally lit allowed",
                    "Permits Required": "Yes",
                    "Mounting": "Wall-mounted only",
                    "Updated": datetime.now().strftime("%Y-%m-%d")
                }
            }
        }
    }
}

with open("burnsville.json", "w") as f:
    json.dump(burnsville_data, f, indent=2)
