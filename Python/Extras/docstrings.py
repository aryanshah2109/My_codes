# Written just after function declaration and before function body
# they can be used in class, modules and methods too
# gives description of what the function does

def square(n):
    '''Takes a number as input and finds square of the number'''
    return n*n
n = int(input("Enter number: "))
print("Square is",square(n))
print("Docstring is:",square.__doc__)


# comments are used to help programmer understand the program but docstring are used to
# document our code

# comments cannot be printed but docstrings can be printed by functionName.__doc__

# PEP-8 stands for Python Enhancement Proposal
# It is a document which best explains the guidelines and best practices to write an
# efficient python program