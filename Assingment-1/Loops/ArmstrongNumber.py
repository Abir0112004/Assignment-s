num = int(input("Enter a number: "))
digits = str(num)
power = len(digits)

sum_power = 0
for d in digits:
    sum_power += int(d) ** power

if sum_power == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
