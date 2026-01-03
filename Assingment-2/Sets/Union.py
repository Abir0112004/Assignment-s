Sentence1 = input("Enter First Sentence: ")
Sentence2 = input("Enter Second Sentence: ")

words1 = Sentence1.split()
words2 = Sentence2.split()
union = set()

for w in words1:
    union.add(w)

for w in words2:
    union.add(w)

print("Union:", union)