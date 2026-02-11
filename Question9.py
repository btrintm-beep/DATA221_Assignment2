import csv
import requests
from bs4 import BeautifulSoup

# Wikipedia page to scrape
page_link = "https://en.wikipedia.org/wiki/Machine_learning"

# Send request with User-Agent so Wikipedia responds normally
request_headers = {"User-Agent": "Mozilla/5.0"}
page_response = requests.get(page_link, headers=request_headers)

# Parse the HTML
html_doc = BeautifulSoup(page_response.text, "html.parser")

# Locate the main article content
article_content = html_doc.find("div", id="mw-content-text")

# Identify the first table with at least 3 data rows
selected_table = None

for tbl in article_content.find_all("table"):
    table_rows = tbl.find_all("tr")
    valid_data_rows = sum(1 for row in table_rows if row.find_all("td"))

    if valid_data_rows >= 3:
        selected_table = tbl
        break

# Extract all rows from the selected table
table_rows = selected_table.find_all("tr")

# Determine column headers
header_cells = table_rows[0].find_all("th")
if header_cells:
    column_names = [cell.get_text(strip=True) for cell in header_cells]
else:
    # Fallback: generate generic column names
    max_columns = max(len(row.find_all("td")) for row in table_rows)
    column_names = [f"col{i+1}" for i in range(max_columns)]

# Extract row data
table_data = []
expected_cols = len(column_names)

for row in table_rows:
    data_cells = row.find_all("td")
    if not data_cells:
        continue

    row_values = [cell.get_text(" ", strip=True) for cell in data_cells]

    # Ensure consistent column count
    if len(row_values) < expected_cols:
        row_values.extend([""] * (expected_cols - len(row_values)))
    elif len(row_values) > expected_cols:
        row_values = row_values[:expected_cols]

    table_data.append(row_values)

# Write extracted table to CSV
with open("wiki_table.csv", "w", newline="", encoding="utf-8") as output_csv:
    csv_writer = csv.writer(output_csv)
    csv_writer.writerow(column_names)
    csv_writer.writerows(table_data)

print("Saved table to wiki_table.csv")
print("Rows saved:", len(table_data))
