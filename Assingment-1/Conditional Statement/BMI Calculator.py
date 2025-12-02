height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

bmi = weight / (height ** 2)
print("Your BMI:", bmi)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal")
elif 25 <= bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")
