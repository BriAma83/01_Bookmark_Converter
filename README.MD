# 🔖 Bookmark Converter

A Python-based automation tool that converts bookmark collections between HTML, Excel, and browser bookmark formats.

## Overview

Many bookmark repositories are maintained in Word documents, exported HTML files, or manually managed browser folders. This project simplifies bookmark management by converting bookmarks into a structured Excel repository and generating browser-compatible bookmark files.

---

## Features

✅ Convert HTML bookmark collections to Excel

✅ Maintain bookmark data in a structured repository

✅ Generate Chrome-compatible bookmark files

✅ Generate Microsoft Edge-compatible bookmark files

✅ Preserve folder and subfolder hierarchy

✅ Simplify ongoing bookmark maintenance

---

## Workflow

```text
HTML Bookmark File
        ↓
HTML_To_Excel.py
        ↓
Excel Repository
        ↓
Excel_To_Bookmarks.py
        ↓
Chrome / Edge Bookmark File
```

---

## Sample Folder Structure

```text
SO Favourite Links
│
├── Knowledge Base
├── Communications
├── Forms
│   ├── Internal
│   └── External
├── Training
├── Analytics
├── Tools
└── Reference
    ├── Guides
    └── Templates
```

---

## Repository Structure

```text
Bookmark_Converter
│
├── Scripts
│   ├── HTML_To_Excel.py
│   └── Excel_To_Bookmarks.py
│
├── Sample_Data
│   ├── Sample_Bookmarks.html
│   └── Sample_Favorites_Links_Master.xlsx
│
├── Output
│   └── Sample_Chrome_Bookmarks.html
│
└── README.md
```

---

## Sample Excel Structure

| ID | Main Folder | Subfolder | Bookmark Name | URL |
|----|------------|------------|------------|-----|
| 1 | Knowledge Base | | Company Knowledge Portal | https://knowledge.example.com |
| 2 | Communications | | Daily News Hub | https://news.example.com |
| 3 | Forms | Internal | Expense Claim Form | https://forms.example.com/expense |

---

## Technologies Used

- Python
- Pandas
- OpenPyXL
- BeautifulSoup4
- HTML
- Excel

---

## Use Cases

- Browser bookmark management
- Bookmark migration projects
- Bookmark standardization
- Bookmark repository maintenance
- Knowledge management initiatives

---

## Future Enhancements

- Dead link detection
- URL validation
- Bookmark deduplication
- SharePoint exports
- Power BI reporting
- Automated bookmark synchronization

---

## Author

Amanda Briell

Senior Business Consultant | Data Analytics | Process Improvement | Automation
