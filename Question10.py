def search_lines_for_term(file_name, search_term):
    """
    Scans a text file and returns a list of (line_index, content)
    for every line that contains the given term, ignoring case.
    Line numbering begins at 1.
    """
    found_lines = []

    with open(file_name, "r", encoding="utf-8") as text_file:
        for line_num, line_content in enumerate(text_file, start=1):
            if search_term.lower() in line_content.lower():
                found_lines.append((line_num, line_content.strip()))

    return found_lines


# try out the function
results = search_lines_for_term("sample-file (1).txt", "lorem")

# show total matches
print("Number of matching lines:", len(results))

# display the first three matches
print("First 3 matching lines:")
for idx, line_text in results[:3]:
    print(idx, line_text)
