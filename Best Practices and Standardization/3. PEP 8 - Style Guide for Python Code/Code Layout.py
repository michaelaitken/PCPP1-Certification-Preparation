'''
=== Indentation ===
'''

# INCORRECT / NOT RECOMMENDED
def my_fun_one(x, y):
    return x * y

def my_fun_two(a, b):
  return a + b

# CORRECT / RECOMMENDED
def my_function(x, y):
    return x * y


'''
=== Continuation Lines ===
'''

# INCORRECT / NOT RECOMMENDED
my_list_one = [1, 2, 3,
    4, 5, 6
]

a = my_function_name(a, b, c,
    d, e, f)


# CORRECT / RECOMMENDED
my_list_one = [
    1, 2, 3,
    4, 5, 6,
    ]

a = my_function_name(a, b, c,
                       d, e, f)

# OR
my_list_two = [
    1, 2, 3,
    4, 5, 6,
]

def my_fun(
        a, b, c,
        d, e, f):
    return (a + b + c) * (d + e + f)

'''
=== Maximum Line Length and Line Breaks ===
If possible, you should limit all lines to a maximum of 79 characters
In the case of docstrings and comments, the line length should not exceed 72 characters.
'''

'''
=== Line breaks and operators ===
'''

# CORRECT / RECOMMENDED
total_fruits = (apples
                + pears
                + grapes
                - (black currants - red currants)
                - bananas
                + oranges)

'''
=== Blank Lines ===
TWO BLANK LINES to surround top-level function and class definitions
SINGLE BLANK LINE to surround method definitions inside a class
BLANK LINES in functions in order to indicate logical sections (sparingly)
'''

'''
=== IMPORTS ===
'''

# INCORRECT / NOT RECOMMENDED
import sys, os

from animals import *


# CORRECT / RECOMMENDED

import os
import sys

from subprocess import Popen, PIPE

import animals.mammals.dogs.puppies


'''
=== Whitespace in expressions and statements ===
Generally, you should avoid using too much whitespace, as it makes your code difficult to follow.
Do not use excessive whitespace immediately inside parentheses/brackets/braces, or immediately before a comma/semicolon/colon.
'''

'''
=== Naming Conventions ===

_my_sample_name - a name that starts with a single leading underscore indicates a weak "internal use", e.g., the instruction from SAMPLE import * will not import objects whose names start with an underscore.



'''