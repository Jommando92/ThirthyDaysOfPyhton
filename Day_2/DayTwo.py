#Build in functions for python
#https://docs.python.org/3/library/functions.html

# min() - returns the minimum value of the data type
# max() - returns the maximum value of the data type
# sum() - returns the sum of the data type
# round() - rounds the data type
# abs() - returns the absolute value of the data type
# pow() - returns the power of the data type
# len() - returns the length of the data type
# sorted() - returns the sorted data type
# reversed() - returns the reversed data type
# type() - returns the data type


# Variables - they are store in a computer memory, it can be a name so that cna be easily remembered and used and associated with a
# value. it can be short or long, it can be a letter or a word or a phrase. it can be a number or a letter or a word or a phrase. but
# it is recommended to use a descriptive name for a variable.

# Day 2 - £0 Days of Python programming

# Levl 1
first_name = "Jumar"
last_name = " Quinio Mesicias"
full_name = first_name + last_name
country = "Philippines"
city = "Manila City"
age = 32
year = 1992
is_married = False
is_true = True
is_light_on = False

# Printing the values of the variables
print("First Name: ", first_name)
print("Last Name: ", last_name)
print("Full Name: ", full_name)
print("Country: ", country)
print("City: ", city)
print("Age: ", age)
print("Year: ", year)
print("Is Married: ", is_married)
print("Is True: ", is_true)
print("Is Light On: ", is_light_on)

# Multiple variable in one line
first_name, last_name, country, age, is_married = "Jumar", "Quinio Mesicias", "Philippines", 32, False
print(first_name, last_name, country, age, is_married)

# Level 2

type(first_name)
type(last_name)
type(country)
type(age)
type(is_married)
type(is_true)
type(is_light_on)
print('first_name: ', first_name)
print('last_name: ', last_name)
print('country length: ', len( country))
print(len(first_name) - len(last_name))

num_one = 5
num_two = 4

add = num_one + num_two
sub = num_one - num_two
multi = num_one * num_two
div = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_div = num_one // num_two

print(add, sub, multi, div, remainder, exp, floor_div)

radius = 30
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius
print(area_of_circle, circum_of_circle)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")
print(first_name, last_name, country, age)
