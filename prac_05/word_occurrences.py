"""
Word Occurrences
Estimate: 20 minutes
Actual:    minutes
"""

word_to_count = {}
text = input("Text: ").split()
for word in text:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

for word, count in word_to_count.items():
    print(f"{word}: {count}")

# TODO: sort alphabetically and align columns
