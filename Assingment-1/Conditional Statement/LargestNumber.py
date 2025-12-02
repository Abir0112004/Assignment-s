a = int(input("Enter First Number , a: "))
b = int(input("Enter Second Number, b: "))
c = int(input("Enter Third Number , c: "))

if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)
