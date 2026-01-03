tuple = (10, 20, 30, 20, 40, 50)
target = 20

for i in range(len(tuple)):
    if tuple[i] == target:
        print("Index:", i)
        break
