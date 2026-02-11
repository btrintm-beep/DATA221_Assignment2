import requests
from bs4 import BeautifulSoup

# Target webpage
page_url = "https://en.wikipedia.org/wiki/Data_science"

# Send request with a browser-like header
request_headers = {"User-Agent": "Mozilla/5.0"}
page_response = requests.get(page_url, headers=request_headers)

# Parse the HTML content
parsed_html = BeautifulSoup(page_response.text, "html.parser")

# Get and display the page title
page_title = parsed_html.find("title").get_text(strip=True)
print("Page title:")
print(page_title)

# Locate the main article content
article_body = parsed_html.find("div", id="mw-content-text")

# Collect all paragraph tags
para_elements = article_body.find_all("p")

# Identify the first paragraph with sufficient length
selected_paragraph = ""
for para in para_elements:
    para_text = para.get_text(strip=True)
    if len(para_text) >= 50:
        selected_paragraph = para_text
        break

print("\nFirst paragraph (50+ characters):")
print(selected_paragraph)
