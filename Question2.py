# Read the text file (Windows file path)
input_location = r"C:\Users\btrintm\Downloads\sample-file (1).txt"

with open(input_location, "r", encoding="utf-8") as reader:
    full_text = reader.read()

# Separate text into raw word chunks
raw_words = full_text.split()

# Characters to strip from word edges
edge_punctuation = ".,!?;:'\"()[]{}<>-"

processed_words = []

# Normalize and filter words
for token in raw_words:
    cleaned = token.lower().strip(edge_punctuation)

    # Count alphabetic characters in the word
    letter_count = 0
    for char in cleaned:
        if char.isalpha():
            letter_count += 1

    # Keep words with at least two letters
    if letter_count >= 2:
        processed_words.append(cleaned)

# Create bigrams (two-word sequences)
word_pairs = []

for index in range(len(processed_words) - 1):
    combined = processed_words[index] + " " + processed_words[index + 1]
    word_pairs.append(combined)

# Count how often each bigram appears
pair_frequencies = {}

for pair in word_pairs:
    pair_frequencies[pair] = pair_frequencies.get(pair, 0) + 1

# Sort bigrams by frequency (highest first)
ordered_pairs = sorted(pair_frequencies.items(), key=lambda item: item[1], reverse=True)

# Output the top 5 most common bigrams
for phrase, occurrences in ordered_pairs[:5]:
    print(f"{phrase} -> {occurrences}")
