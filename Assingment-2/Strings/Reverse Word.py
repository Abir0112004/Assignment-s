sentence = "Abir Saha"
words = sentence.split()
result = []

for w in words:
    result.append(w[::-1])

print(" ".join(result))
