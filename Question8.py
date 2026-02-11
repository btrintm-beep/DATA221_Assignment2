import requests
from bs4 import BeautifulSoup

# Wikipedia article to scrape
article_url = "https://en.wikipedia.org/wiki/Data_science"

# Use a browser-like header to avoid blocked responses
request_headers = {"User-Agent": "Mozilla/5.0"}
page_data = requests.get(article_url, headers=request_headers)

# Parse HTML with BeautifulSoup
html_tree = BeautifulSoup(page_data.text, "html.parser")

# Locate the main content area of the page
main_section = html_tree.find("div", id="mw-content-text")

section_titles = []
blocked_sections = ["References", "External links", "See also", "Notes"]

# Extract top-level section headings
for header in main_section.find_all("h2"):
    headline = header.find("span", class_="mw-headline")

    if headline:
        heading_text = headline.get_text(strip=True)
    else:
        heading_text = (
            header.get_text(" ", strip=True)
            .replace("[edit]", "")
            .strip()
        )

    if not any(blocked in heading_text for blocked in blocked_sections):
        section_titles.append(heading_text)

# Write headings to a text file (one per line)
with open("headings.txt", "w", encoding="utf-8") as output_file:
    for title in section_titles:
        output_file.write(title + "\n")

# Print headings for verification
for title in section_titles:
    print(title)
