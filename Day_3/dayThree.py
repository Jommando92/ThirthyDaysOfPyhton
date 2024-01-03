import math


#Boolean  - True or False
# This function converts a value to a boolean (True or False) using the standard truth testing procedure.
print(True)
print(False)

# Day 3 - 30 Days ot Python programming.

# age = 32
# float = 6.2 #foot
# complex = 3.1416j

# print(age,  float, complex)
# print(age + float)

# Area of the triangle

# area = 0.5 * b * h
# b = input("Enter the base of the triangle: ")
# h = input("Enter the height of the triangle: ")
# area = 0.5 * float(b) * float(h)
# print("The area of the triangle is: ",  area)

#Perimeter of a Triangle

#Perimeter = a + b + c

# a = input("Enter Side A: ")
# b = input("Enter Side B: ")
# c = input("Enter side C: ")
# p = float(a) +float(b) + float(c)
# print("The perimeter of the triangle is: ", p)

# Rectangle Area

# # area = length * width // perimeter = 2 * (length + width)
# a = input("Enter Length of the Rectangle: ")
# b = input("Enter width of the rectangle: ")
# area = int(a) * int(b)
# perimeter = 2 * area

# print("this is the area: ", area, "of the rectangle and the perimeter is: ", perimeter)

# Radius of a Circle

# Area = pi * r * r // circumference = 2 * pi* r // pi = 3.14


r = float(input("Enter Radius of the Circle: "))
area = math.pi  * r * r
circumference = 2 * math.pi * r
print(f"This are the area = {area} and the circumference = {round(circumference, 2)} of the circle")

# Calculate slope of y = 2x -2
