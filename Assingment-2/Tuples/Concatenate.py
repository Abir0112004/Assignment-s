tuple1 = (1, 2)
tuple2 = (3, 4)
result = ()

for x in tuple1:
    result += (x,)
for x in tuple2:
    result += (x,)

print(result)

