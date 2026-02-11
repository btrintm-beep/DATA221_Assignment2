import string

# Location of the input text file
source_file = r"C:\Users\btrintm\Downloads\sample-file (1).txt"


# Turn a line into a comparable "signature" so small formatting differences match
def line_signature(raw_line: str) -> str:
    # standardize case
    lowered = raw_line.lower()

    # remove spaces/tabs
    no_spaces = lowered.replace(" ", "")

    # strip punctuation characters
    for symbol in string.punctuation:
        no_spaces = no_spaces.replace(symbol, "")

    return no_spaces


# Load all lines from the file
with open(source_file, "r", encoding="utf-8") as fh:
    all_lines = fh.readlines()

# Map: normalized signature -> list of (line_number, original_text)
signature_map = {}

for idx, line in enumerate(all_lines, start=1):
    original_text = line.strip()

    # ignore blank lines completely
    if original_text == "":
        continue

    signature = line_signature(original_text)

    if signature not in signature_map:
        signature_map[signature] = []

    signature_map[signature].append((idx, original_text))

# Keep only entries where the same signature appears more than once
duplicate_groups = []
for sig, occurrences in signature_map.items():
    if len(occurrences) > 1:
        duplicate_groups.append(occurrences)

# Report results
print("Number of near-duplicate sets:", len(duplicate_groups))

print("\nFirst two sets found:")
for group in duplicate_groups[:2]:
    print("\nSet:")
    for line_no, content in group:
        print(f"{line_no} : {content}")
