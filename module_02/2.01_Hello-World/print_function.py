print("Hello World")

# Print function print()

# print is the name of the function
# A function in python can:
# - cause an effect (send text to the terminal, create a file, draw an image, make a sound)
# = evaluate a value and return it as result of the function

# A function can have his origin from:
# - Built in python functions like print(), len(), str() …
# - Other modules
# - Or from our code (the functions that we can create)

### Function Arguments
# A function can receive one or more arguments (or none)
# The functions always needs parentesis
# print receives as an argument a string
# a string is this → “something wrapped in quotes”

### Escape characters and New Line
print("Hello \nWorld")

# \n → new line

# Multiple Arguments
print("Hello", "World")

# Positional Arguments
# each element in the arguments has a position (0, 1, 2, 3, 4, 5)

# Keyword Arguments
# BEWARE: Each keyword argument must be at the end of the last positional argument

# Known Keywords
# end= at the end of the print
# sep= separator

print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

# example using end and sep

print("Mi", "nombre", "es", sep=" ", end=" *")
print("Monty", "Python", sep="*", end="-peko*\n")

# **`Mi nombre es *Monty*Python-peko*`**

# Arrows Exercise

###################
print("Original Arrow")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("*********")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("Arrow in a single line")
###################
print("    *\n   * *\n  *   *\n *     *\n*********\n  *   *\n  *   *\n  *****")
###################
print("Extended Arrow:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("*****************")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("Double Arrow:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("*****************"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)