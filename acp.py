# Program to calculate trigonometric values using the math module

import math

# Input angle in degrees
angle = float(input("Enter an angle in degrees: "))

# Convert degrees to radians
radian = math.radians(angle)

# Calculate trigonometric values
sin_value = math.sin(radian)
cos_value = math.cos(radian)
tan_value = math.tan(radian)

# Display the results
print("\nTrigonometric Values")
print("--------------------")
print("sin(", angle, ") =", sin_value)
print("cos(", angle, ") =", cos_value)
print("tan(", angle, ") =", tan_value)