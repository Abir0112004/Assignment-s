list = [(1,2,3), (4,5,6)]
result = []

for t in list:
    new_t = (t[-1],) + t[1:-1] + (t[0],)
    result.append(new_t)

print(result)
