import math

# String data types

# literal assignment
first = "Fortune"
last = "Foluso"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# constuructor function
pizza = str('pepperoni')

print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock movies from the " + decade
print(statement)

multiline = '''This is python

                Just lines of code that does stuff
'''

print(multiline)

# Escaping special characters

sentence = 'I\'m soo stupid! \t is should just go back to sleep. \nCant\'t even sleep properly (\-_-/)'
print(sentence)

# String Methods
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("code", "....."))
print(multiline)

print(len(multiline))
multiline +="                                         "
multiline = "                                         " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print()

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, '.') + "$1".rjust(4))
print("Muffin".ljust(16, '.') + "$2".rjust(4))
print("Cheesecake".ljust(16, '.') + "$3".rjust(4))

print()

# string index values
print(first[1])
print(first[-1])
print(first[0:])

# Some method return boolean data
print(first.startswith("F"))
print(first.endswith("s"))

# Boolean data types
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

# Numeric Data Types
price = 100
best_price = int(1000)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28

y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))
print ("I am incredibly slow and bad at typing")