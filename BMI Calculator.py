5
# Simple BMI Calculator for Beginners

print("=== BMI CALCULATOR ===")

# Taking input from user
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculating BMI
bmi = weight / (height * height)

# Showing result
print("Your BMI is:", round(bmi, 2))

# Checking category
if bmi < 18.5:
    print("You are Underweight.")
elif bmi < 25:
    print("You have Normal weight.")
elif bmi < 30:
    print("You are Overweight.")
else:
    print("You are Obese.")