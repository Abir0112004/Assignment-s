temp = float(input("Enter temperature in Celsius: "))

if temp > 0:
    fahrenheit = (temp * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
else:
    kelvin = temp + 273.15
    print("Temperature in Kelvin:", kelvin)
