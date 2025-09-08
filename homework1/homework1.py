# File: homework1.py

# --- Variables and Data types ---

a = 10
print(a)
print(type(a))
# this is an integer (int), a whole number

b = 1.5
print(b)
print(type(b))
# this is a float, a number with decimal places

c = 3j
print(c)
print(type(c))
# this is an imaginary number, the product of a real number and the imaginary unit j (sqrt(-1))

d = "hello"
print(d)
print(type(d))
# this is a string, a sequence of characters enclosed in quotes

e = [1,2,3]
print(e)
print(type(e))
# this is a list of integers, an ordered changable sequence of elements

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
# this is a dictionary, an unordered collection storing data in key-value pairs

g = (1,2)
print(g)
print(type(g))
# this is a tuple, an immutable sequence

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
# this is a list of strings

i = True
print(i)
print(type(i))
# this is a boolean, used in conditional statements, and are case sensitive

j = None
print(j)
print(type(j))
# this is a NoneType, a constant representing the absence of a value

k = [True, "blue", 12]
print(k)
print(type(k))
# this is a list containing different data types

l = str(14)
print(l)
print(type(l))
# this is a string, specifically a function that converts what would be (on its own) something else (in this case an integer) to a string

m = 1e4
print(m)
print(type(m))
# this is a float; in python, any value represented by exponent is also a float

# --- Questions ---
    #1) 9 different data types
    #2) int, float, complex, string, list, dict, typle, bool, NoneType
    #3) float: b, e; str: d, l; list: e, h, k
    #4) l is a str, it is not an integer because we called an operation to change it to a string; str() is an operation that changes a variable to having the str property
    #5

o = range(7)
print(o)
print(type(o))
# this is a range, representing a set of values with a defined beginning an end

# --- Booleans ---
print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 is not equal to 9
print(10 <= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, the boolean is not empty
print(bool(123)) # True, the boolean is not empty, any non zero number is considered True
print(bool(["apple", "cherry", "banana"])) # True, non empty lists are True
print(bool(True)) # True, a True boolean itself is True
print(bool(False)) # False, a False boolean itself is False
print(bool(0)) # False, the interger 0 is considered False
print(bool("")) # False, an empty string is False
print(bool(" ")) # True, a string of a space is considered non empty and therefore True
print(bool(())) # False, an empty tuple is False
print(bool([])) # False, an empty list is False
print(bool({})) # False, an empty dictionary is False 
print(bool(True and False)) # False, and operator returns False if any operand is False
print(bool(True and True)) # True, and returns True if and only if both operands are True
print(bool(False and False)) # False, and operator returns False if any operand is False
print(bool(True or False)) # True, or operator returns True if at least one operand is True
print(bool(True or True)) # True, same as above
print(bool(False or False)) # False, or returns False if and only if both operands are False
print(bool(not(False))) # True, not negates False to True
print(bool(not(True))) # False, not negates True to False

# --- Questions ---
    # for an and operator, it will only return True if and only if at least one operand is True
    # I am surprised about False and False being False
    
print(bool("False")) #True, a non empty string returns True even if it contains the word False
print(bool(set())) #False, an empty set is False







