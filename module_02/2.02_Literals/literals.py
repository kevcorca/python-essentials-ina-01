### Integer
print(2)
# Every type of number that any modern computer can handle are:
# - Integer (without decimal numbers)
# - Float (numbers with decimals)
# Python can’t handle comas or dots on integers, only permits this → _
# Integers can accept negative numbers

### Octal and hexadecimal numbers

# If the number starts with ZERO-o (0o or 0O) it will be treated as an octal number, it means that the number only contains numbers from the range 0..7
# 0o123 = 83

print(0o123)

# output → 83

# hexadecimal starts with ZERO-x (0x or 0X)

print(0x123)

# output → 291

### Floats on python
print(2.02)
# Floats are the numbers that have a decimal part, you need to use dot, not comma, because the language will not allow it and return an error if you try it
# E or e (exponente)
# print(3E8)

### Strings on python
print("this is a string")
# You need strings when you need to process data in form of text, not numbers
# always requires quotes
# “this is a string”
# you can use an apostrofe instead of quotes
# ‘my name is “Monty Python”’
# or you can also use escape characters
# “my name is \”Monty Python\””

### Booleans on python
print(True)
# Uses the veracity
# If you ask for example if a number is greater than other number it returns a boolean (True or False)
# George Boole (1815-1864), author of Las Leyes del Pensamiento
# Algebra uses two answers:
# True
# False

# LAB Literales de Python - Cadenas
# Write code consisting of one line of code using the function print(), newline and escape characters, that prints the following text
# "Estoy"""aprendiendo"""""Python"""
print('"Estoy"""aprendiendo"""""Python"""')
