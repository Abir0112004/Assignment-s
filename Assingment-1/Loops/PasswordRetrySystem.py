password = "AbirSaha123"
attempts = 0

while attempts < 3:
    u = input("Enter password: ")
    if u == password:
        print("Access Granted")
        break
    else:
        print("Wrong password")
        attempts += 1

if attempts == 3:
    print("Account locked")
