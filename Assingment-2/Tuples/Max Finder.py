tuple = (5, 2, 9, 1, 7, 0, 4)
max_value = min_value = tuple[0]

for n in tuple:
    if n > max_value:
        max_value = n
    if n < min_value:
        min_value = n

print("Max Value:", max_value)
print("Min Value:", min_value)