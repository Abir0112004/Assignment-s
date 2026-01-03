nums = [3, -1, 5, -7, 0, -2]
positive = []
negative = []

for n in nums:
    if n >= 0:
        positive.append(n)
    else:
        negative.append(n)

print("Positive:", positive)
print("Negative:", negative)
