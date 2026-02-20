def count_frequencies(text):
    frequency = {} # dictionary to store word frequencies
    for word in text.split():
        word = word.lower().strip('.,!?";()') # strip() is used to remove punctuation from the word
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

text = "This is a sample text for frequency counting. This text is just a sample."
frequencies = count_frequencies(text)
for word, count in frequencies.items():
    print(f"{word}: {count}")