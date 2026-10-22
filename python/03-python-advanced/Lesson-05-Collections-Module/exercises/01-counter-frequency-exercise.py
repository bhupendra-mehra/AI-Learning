from collections import Counter

text = """
python ai python machine learning
ai python deep learning machine learning
"""

words = text.split()

word_count = Counter(words)

print(word_count)
print(word_count.most_common(3))