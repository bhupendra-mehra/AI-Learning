from collections import Counter

items = ["apple", "apple", "banana", "apple", "orange","watermelon", "banana", "kiwi", "watermelon", "kiwi"]

counts = Counter(items)

print(counts)

print(counts['apple'])

print(counts.most_common(2))


text = "python is easy and python is powerful"

words = text.split()

word_counts = Counter(words)

print(word_counts)

print(word_counts.most_common(2))