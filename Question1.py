# Load the text file from your Downloads folder (Windows path)
source_path = r"C:\Users\btrintm\Downloads\sample-file (1).txt"

with open(source_path, "r", encoding="utf-8") as infile:
    raw_text = infile.read()

# Break the text into rough "word-like" pieces
raw_parts = raw_text.split()

# Characters to trim off the ends of words (basic punctuation + brackets, etc.)
trim_chars = ".,!?;:'\"()[]{}<>-"

filtered_words = []

for piece in raw_parts:
    normalized = piece.lower().strip(trim_chars)

    # Only keep tokens that contain at least two alphabetic letters
    letter_total = sum(1 for c in normalized if c.isalpha())
    if letter_total >= 2:
        filtered_words.append(normalized)

# Build a frequency table (word -> occurrences)
freq_table = {}
for token in filtered_words:
    freq_table[token] = freq_table.get(token, 0) + 1

# Rank words by frequency (highest first)
ranked = sorted(freq_table.items(), key=lambda pair: pair[1], reverse=True)

# Display the 10 most common words
for term, hits in ranked[:10]:
    print(f"{term} -> {hits}")
