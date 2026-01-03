tuple = (1, 2, 3, 4, 5)

for i in range(len(tuple)):
    for j in range(i+1, len(tuple)):
        if (tuple[i] + tuple[j]) % 2 == 0:
            print(tuple[i], tuple[j])
