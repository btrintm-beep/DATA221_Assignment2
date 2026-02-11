# DATA221_Assignment2
# Text Analysis, Data Processing, and Web Scraping Toolkit

This repository contains a collection of Python scripts focused on **text processing**, **data analysis with pandas**, and **web scraping using BeautifulSoup**. Each script performs a specific task and is written to be clear, modular, and reusable.

---

## 📁 Contents Overview

### 1. Text Cleaning & Word Frequency
- Reads a text file
- Normalizes words (lowercase, removes punctuation)
- Filters words with at least 2 alphabetic characters
- Counts word frequencies
- Prints the top most common words

**Key concepts:** file I/O, string processing, dictionaries

---

### 2. Bigram Frequency Analysis
- Cleans text using the same normalization rules
- Builds **bigrams** (pairs of consecutive words)
- Counts how often each bigram appears
- Prints the top 5 most frequent bigrams

**Key concepts:** tokenization, sequence analysis

---

### 3. Near-Duplicate Line Detection
- Normalizes lines by removing spaces, punctuation, and case differences
- Groups lines that are “nearly identical”
- Reports how many duplicate groups exist
- Prints example duplicate sets with line numbers

**Key concepts:** text normalization, hashing/grouping

---

### 4. Student Engagement Filtering (CSV)
- Loads student data from `student.csv`
- Filters students based on:
  - Study time
  - Internet access
  - Low absences
- Saves filtered results to `high_engagement.csv`
- Prints summary statistics

**Key concepts:** pandas filtering, CSV output

---

### 5. Student Grade Band Summary
- Categorizes students into **Low / Medium / High** grade bands
- Computes:
  - Number of students per band
  - Average absences
  - Internet access percentage
- Saves results to `student_bands.csv`

**Key concepts:** pandas `groupby`, aggregation

---

### 6. Crime & Unemployment Analysis
- Loads crime data from `crime.csv`
- Labels rows as **HighCrime** or **LowCrime**
- Calculates average unemployment rate for each category
- Prints results clearly

**Key concepts:** conditional labeling, grouped statistics

---

### 7. Wikipedia Page Content Extraction
- Fetches a Wikipedia article using `requests`
- Extracts and prints:
  - Page title
  - First paragraph with 50+ characters

**Key concepts:** HTTP requests, HTML parsing

---

### 8. Wikipedia Section Heading Scraper
- Extracts all main section headings (`<h2>`) from a Wikipedia page
- Excludes non-content sections (References, Notes, etc.)
- Saves headings to `headings.txt`

**Key concepts:** DOM traversal, filtering content

---

### 9. Wikipedia Table to CSV
- Finds the first table with meaningful data (≥ 3 rows)
- Extracts headers and rows
- Normalizes row lengths
- Saves the table to `wiki_table.csv`

**Key concepts:** web scraping, structured data extraction

---

### 10. Keyword Line Search Utility
- Searches a text file for lines containing a keyword
- Case-insensitive matching
- Returns line numbers and text
- Prints count and first few matches

**Key concepts:** reusable functions, text search

---

## 🛠 Requirements

- Python 3.x  
- Required libraries:
  ```bash
  pip install pandas requests beautifulsoup4
