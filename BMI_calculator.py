#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     11/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in inches: "))

# Convert height from inches to meters
height_m = height * 0.0254

# Calculate BMI
bmi = weight / (height_m ** 2)

print(f"Your BMI is: {bmi:.2f}")
  # BMI Categories
if bmi < 18.5:
  print("You are Underweight")
elif 18.5 <= bmi < 24.9:
  print("You are Normal weight")
elif 25 <= bmi < 29.9:
  print("You are Overweight")
else:
  print("You are Obese")

