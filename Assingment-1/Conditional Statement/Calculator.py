a = float(input("Enter First  Number : "))
b = float(input("Enter Second Number : "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    if b == 0:
        print("Syntax Error : Division by zero is not allowed.")
    else:
        print("Result:", a / b)
else:
    print("Invalid operator")
