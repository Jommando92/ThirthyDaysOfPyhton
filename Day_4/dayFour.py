# letter = 'P'                # A string could be a single character or a bunch of texts
# print(letter)               # P
# print(len(letter))          # 1
# greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
# print(greeting)             # Hello, World!
# print(len(greeting))        # 13
# sentence = "I hope you are enjoying 30 days of Python Challenge"
# print(sentence)
# # using ('''   ''')
# multiline_string = '''I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python.'''
# print(multiline_string)

# # Another way of doing the same thing (""" """)
# multiline_string = """I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python."""
# print(multiline_string)


# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# space = ' '
# full_name = first_name  +  space + last_name
# print(full_name) # Asabeneh Yetayeh
# # Checking the length of a string using len() built-in function
# print(len(first_name))  # 8
# print(len(last_name))   # 7
# print(len(first_name) > len(last_name)) # True
# print(len(full_name)) # 16

"""
# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")
"""

# print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
# print('Days\tTopics\tExercises') # adding tab space or 4 spaces
# print('Day 1\t5\t5')
# print('Day 2\t6\t20')
# print('Day 3\t5\t23')
# print('Day 4\t1\t35')
# print('This is a backslash  symbol (\\)') # To write a backslash
# print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

"""
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.number of digitsf" - Floating point numbers with fixed precision
"""

# # Strings only
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# print(formated_string)

# # Strings  and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

# python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
# formated_string = 'The following are python libraries:%s' % (python_libraries)
# print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"



#  New formated_string

# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
# print(formated_string)
# a = 4
# b = 3

# print('{} + {} = {}'.format(a, b, a + b))
# print('{} - {} = {}'.format(a, b, a - b))
# print('{} * {} = {}'.format(a, b, a * b))
# print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
# print('{} % {} = {}'.format(a, b, a % b))
# print('{} // {} = {}'.format(a, b, a // b))
# print('{} ** {} = {}'.format(a, b, a ** b))

# # Strings  and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
# print(formated_string)


# f-String - this will allows to insert the data to the corresponding place.

# a = 4
# b = 3
# print(f'{a} + {b} = {a +b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')
# print(f'{a} / {b} = {a / b:.2f}')
# print(f'{a} % {b} = {a % b}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} ** {b} = {a ** b}')

# Day Four for Python Learning

# sentence = ['Thirty' ,'Days', 'Of', 'Phyton']
# result = ' '.join(sentence)
# print(result)

# strOne = "Coding"
# strTwo = "For"
# strThree = "All"
# print(strOne, strTwo, strThree)

company = "Coding For All"
print(len(company))
print((company))