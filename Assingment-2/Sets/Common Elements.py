a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
common = []

for x in a:
    if x in b:
        common.append(x)

print(common)
