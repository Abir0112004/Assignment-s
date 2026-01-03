list = [1, 2, 2, 3, 1, 4, 2, 1, 4, 5, 3, 2, 1]
frequency = {}

for item in list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)

