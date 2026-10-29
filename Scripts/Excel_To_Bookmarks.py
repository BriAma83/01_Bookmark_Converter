import pandas as pd
from html import escape

INPUT_FILE = "Sample_Favorites_Links_Master.xlsx"
OUTPUT_FILE = "Sample_Favourite_Links_Bookmarks.html"

# Read Excel
df = pd.read_excel(INPUT_FILE)

# Keep only Active bookmarks if Status column exists
if "Status" in df.columns:
    df = df[df["Status"].fillna("Active").str.strip() == "Active"]

# Replace blank values
df["Main Folder"] = df["Main Folder"].fillna("")
df["Subfolder"] = df["Subfolder"].fillna("")
df["Bookmark Name"] = df["Bookmark Name"].fillna("")
df["URL"] = df["URL"].fillna("")

html = []

# Netscape Bookmark Header
html.append("""<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file. -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>

<DL><p>
    <DT><H3>My Favourite Links</H3>
    <DL><p>
""")

# Process Main Folders
for main_folder in sorted(df["Main Folder"].unique()):

    folder_df = df[df["Main Folder"] == main_folder]

    html.append(
        f'        <DT><H3>{escape(str(main_folder))}</H3>\n'
        f'        <DL><p>\n'
    )

    # Bookmarks with no subfolder
    root_rows = folder_df[
        folder_df["Subfolder"].astype(str).str.strip() == ""
    ]

    for _, row in root_rows.iterrows():

        bookmark_name = escape(str(row["Bookmark Name"]))
        url = escape(str(row["URL"]))

        html.append(
            f'            <DT><A HREF="{url}">{bookmark_name}</A>\n'
        )

    # Process Subfolders
    subfolders = sorted(
        [
            sf
            for sf in folder_df["Subfolder"].unique()
            if str(sf).strip() != ""
        ]
    )

    for subfolder in subfolders:

        html.append(
            f'            <DT><H3>{escape(str(subfolder))}</H3>\n'
            f'            <DL><p>\n'
        )

        sub_df = folder_df[
            folder_df["Subfolder"] == subfolder
        ]

        for _, row in sub_df.iterrows():

            bookmark_name = escape(str(row["Bookmark Name"]))
            url = escape(str(row["URL"]))

            html.append(
                f'                <DT><A HREF="{url}">{bookmark_name}</A>\n'
            )

        html.append(
            '            </DL><p>\n'
        )

    html.append(
        '        </DL><p>\n'
    )

# Closing Tags
html.append("""
    </DL><p>
</DL><p>
""")

# Write File
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("".join(html))

print()
print("=" * 50)
print("BOOKMARK FILE CREATED")
print("=" * 50)
print(f"Output: {OUTPUT_FILE}")
print("=" * 50)
