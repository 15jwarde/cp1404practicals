"""
Word Occurrences
Estimate: 20 minutes
Actual:   27 minutes
"""

word_to_count = {}
text = input("Text: ").split()
for word in text:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

longest_word = -1
# for word in word_to_count:

for word, count in sorted(word_to_count.items()):
    print(f"{word}: {count}")

# TODO: add column formatting
