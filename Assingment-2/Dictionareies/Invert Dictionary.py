Dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}
invert = {}

for key, value in Dictionary.items():
    invert[value] = key

print(invert)
