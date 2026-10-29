import pandas as pd
import re
from bs4 import BeautifulSoup

# --------------------------------------------------
# Configuration
# --------------------------------------------------

HTML_FILE = "Sample_Bookmarks.html"
OUTPUT_FILE = "Sample_Favorites_Links_Master.xlsx"

# --------------------------------------------------
# Read HTML
# --------------------------------------------------

with open(HTML_FILE, "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# --------------------------------------------------
# Storage
# --------------------------------------------------

rows = []

current_folder = ""
current_subfolder = ""

# --------------------------------------------------
# Process HTML Elements
# --------------------------------------------------

for element in soup.find_all(["h1", "h2", "p"]):

    # Main Folder
    if element.name == "h1":
        current_folder = element.get_text(" ", strip=True)
        current_subfolder = ""

    # Subfolder
    elif element.name == "h2":
        current_subfolder = element.get_text(" ", strip=True)

    # Bookmark Entry
    elif element.name == "p":

        text = element.get_text(" ", strip=True)

        # Skip blank rows
        if not text:
            continue

        html_text = str(element)

        # Extract URL
        urls = re.findall(r'https?://[^"<>\s]+', html_text)

        if urls:

            url = urls[0]

            # Clean up URL encoding
            url = url.replace("&amp;", "&")

            rows.append({
                "ID": len(rows) + 1,
                "Main Folder": current_folder,
                "Subfolder": current_subfolder,
                "Bookmark Name": text,
                "URL": url,
                "Active": "Y",
                "Notes": ""
            })

# --------------------------------------------------
# Build DataFrame
# --------------------------------------------------

df = pd.DataFrame(rows)

# Ensure column order
df = df[
    [
        "ID",
        "Main Folder",
        "Subfolder",
        "Bookmark Name",
        "URL",
        "Active",
        "Notes"
    ]
]

# --------------------------------------------------
# Export Excel
# --------------------------------------------------

with pd.ExcelWriter(
    OUTPUT_FILE,
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        sheet_name="Bookmarks",
        index=False
    )

    worksheet = writer.sheets["Bookmarks"]

    # Auto-size columns
    for column in worksheet.columns:
        max_length = 0
        column_letter = column[0].column_letter

        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass

        worksheet.column_dimensions[column_letter].width = min(max_length + 2, 75)

# --------------------------------------------------
# Summary
# --------------------------------------------------

print()
print("====================================")
print(" Conversion Complete")
print("====================================")
print(f" Bookmarks Extracted : {len(df)}")
print(f" Output File         : {OUTPUT_FILE}")
print("====================================")
print()
