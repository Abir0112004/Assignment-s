Sentence = "Umbrella"
frequency = {}

for ch in Sentence:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print(frequency)