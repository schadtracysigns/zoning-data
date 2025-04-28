import json
import os

def merge_json_files(output_file, input_files):
    combined_data = []

    for file_path in input_files:
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                data = json.load(f)
                combined_data.append(data)

    with open(output_file, "w") as f:
        json.dump(combined_data, f, indent=2)

if __name__ == "__main__":
    merge_json_files(
        "zoning_combined.json",
        ["burnsville.json", "rochester.json"]
    )
