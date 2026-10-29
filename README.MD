# Bookmark Converter

A Python-based automation tool that converts bookmark collections between HTML, Excel, and browser bookmark formats.

## Overview

This project was created to modernize and maintain large bookmark repositories that were originally stored in Word and HTML formats.

The solution:

1. Extracts bookmarks from legacy HTML files.
2. Converts bookmark information into a structured Excel repository.
3. Generates Chrome and Microsoft Edge compatible bookmark files.
4. Preserves folder and subfolder hierarchy.
5. Simplifies long-term bookmark maintenance.

## Features

- HTML to Excel conversion
- Excel to browser bookmark conversion
- Chrome-compatible bookmark export
- Microsoft Edge-compatible bookmark export
- Folder and subfolder support
- Structured bookmark repository
- Easy maintenance through Excel

## Technologies

- Python
- pandas
- openpyxl
- BeautifulSoup

## Workflow

Legacy HTML
↓
Excel Repository
↓
Bookmark Generator
↓
Chrome / Edge Bookmark File

## Sample Structure

SO Favourite Links
├── Communications & News
├── Manuals
├── Job Aids
├── Forms
│   ├── Provincial
│   └── Federal
├── Programs and Tools
├── IT
└── Training

## Future Enhancements

- Bookmark validation
- Dead link detection
- SharePoint exports
- Power BI reporting
- Automated bookmark synchronization