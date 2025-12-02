num = int(input("Enter A Number: "))
renum = 0

while num > 0:
    digit = num % 10
    renum = renum * 10 + digit
    num //= 10

print("Reversed Number: ", renum)
