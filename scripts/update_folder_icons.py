# 🚀 python scripts/update_folder_icons.py

import os
import json
import re

# Path to your project (current folder)
project_path = os.getcwd()

# Define icon mapping based on first digit of prefix
# Website for folder names: https://gist.github.com/rupeshtiwari/6860fbc1b3e2f6711c780070d6f59748
icon_mapping = {
    "0": "Mock",      
    "1": "Download",  
    "2": "Tools",      
    "3": "Graphql", 
    "4": "Global",
    "5": "Batch",
    "6": "Messages",
    "7": "Circleci",
    "9": "EMPTY BLACK LINE"
}

# Regex pattern for folders like "000 - Something"
pattern = re.compile(r'^(\d{3})\s*-\s*.*')

# Dictionary to store folder associations
folder_associations = {}

# Recursive scan function
def scan_folders(path):
    for item in os.listdir(path):
        folder_path = os.path.join(path, item)
        if os.path.isdir(folder_path):

            # ✅ Direct rule: if folder is literally named "leetcode"
            # if item.lower() == "leetcode":
            #     rel_path = os.path.relpath(folder_path, project_path)
            #     folder_associations[rel_path.replace("\\", "/")] = "Src"

            # ✅ Prefix rule: if folder matches "000 - Something"
            match = pattern.match(item)
            if match:
                first_digit = match.group(1)[0]
                icon = icon_mapping.get(first_digit, "Folder")
                rel_path = os.path.relpath(folder_path, project_path)
                folder_associations[rel_path.replace("\\", "/")] = icon

            # Recurse into subfolder
            scan_folders(folder_path)

# Start scanning from project root
scan_folders(project_path)

# Create VSCode JSON
vscode_json = {
    "material-icon-theme.folders.associations": folder_associations
}

# Save to .vscode/settings.json
vscode_folder = os.path.join(project_path, ".vscode")
os.makedirs(vscode_folder, exist_ok=True)
settings_file = os.path.join(vscode_folder, "settings.json")
with open(settings_file, "w") as f:
    json.dump(vscode_json, f, indent=4)

print(f"VSCode folder associations generated at {settings_file}")
