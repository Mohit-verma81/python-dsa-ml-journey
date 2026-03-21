def word_count(text):
    words = text.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


sentence = input("Enter a sentence: ")
result = word_count(sentence)

for word, count in result.items():
    print(f"{word}: {count}")