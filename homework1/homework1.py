#File: homework1. py

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

# --- Artithmetic Operators ---

print(10 + 5) # 15, performs addition
print(10 - 5) # 5, subtraction
print(2 * 4) # 8, multiplication
print(6 / 3) # 2, division
print(5 % 2) # 1, modular
print(3 ** 2) # 9, exponent
print(15 // 2) # 7, floor division

# --- Comparison Operators ---

print(5 == 2) # False, 5 is not equal to 2
print(10 != 10) # False, 10 is not not equal to 10
print(2 < 5) # True, 2 is less than 5
print(12 > 5) # True, 12 is greater than 5
print(5 <= 6) # True, 5 is less than or equal to 6
print(1 >= 10) # False, 1 is not greater than or equal to 10

# --- Assignments Operators ---

x = 5
print(x)
x += 5 
print(x)
x -= 4 
print(x)
x *= 3 
print(x)

# --- Logical Operators ---
# 1. What does the operator and do? 
# The 'and' operator returns True if both operands are True, otherwise returns False.

# Write an expression that results in True:
print((5 > 3) and (10 < 15))  # True, because both conditions are True

# Write an expression that results in False:
print((5 > 3) and (10 > 15))  # False, because second condition is False

# 2. What does the operator or do?
# The 'or' operator returns True if at least one operand is True, otherwise returns False.

# Write an expression that results in True:
print((5 > 3) or (10 > 15))  # True, because first condition is True

# Write an expression that results in False:
print((5 < 3) or (10 > 15))  # False, because both conditions are False

# 3. What does the operator not do?
# The 'not' operator returns the opposite boolean value (negates the operand).

# Write an expression that results in True:
print(not (5 > 10))  # True, because 5>10 is False, and not False is True

# Write an expression that results in False:
print(not (5 < 10))  # False, because 5<10 is True, and not True is False

# 1. What is the difference between / and //?
# / is regular division (returns float), // is floor division/function (returns integer, rounds down to nearest whole number)

# 2. What is the difference between % and //?
# % is modulus (returns the remainder after division), // is floor division (returns quotient as integer rounded down to the nearest whole number)

#3. What operator would you use to calculate the remainder when dividing two numbers?
# The modulus operator % 

r = 10 % 3  # 10/3 = 3 r 1, so should return 1
print(r) # prints 1

# 4. How do assignment operators work?
# Assignment operators combine an arithmetic operation (mentioned above) with assignment of the value to the variable after the operation; the variable on the left with the operation on the right


# --- Strings ---

my_string = "hello"

print(my_string) # hello
print(my_string[0]) # h, first letter of hello/0th letter of the str
print(my_string[1]) # e
print(my_string[2]) # l
print(my_string[3]) # l 
print(my_string[4]) # o
print(my_string[-1]) # o, -1st letter is the last letter of the str
print(my_string[1:3]) # el, 
print(my_string[0:5:2]) # hlo
print(len(my_string)) # length of str/number of letters in hello is 5
print(len(my_string) + len("goodbye")) # 5 + 7 = 12
print(len(my_string) * 7) # 5 * 7 = 35

# --- Questions ---

"""
#1.
Slicing is extracting a portion of a string by specifying start and end indices: string[start:end:step]
For these two operations: we used slicing:

print(my_string[1:3]) # el, 
print(my_string[0:5:2]) # hlo

"""

# 2.
name = "Oski"
print("Hello, my name is", name)
# Result: "Hello, my name is Oski"

# 3.
name = "Oski"
print(f"Hello, my name is {name}")
# Result: "Hello, my name is Oski" 

# 4.
"""
The key differences are that:
1. The first version uses comma separation, which automatically adds a space in Python
2. Second version uses f-string which inserts the variable directly into the string template

"""

"""
Terminal Commands:

cd: change directory, use to move from one folder to another, ex. cd sarayu
ls: shows all contents of a specific folder, ex. ls python_decal_fa25
ls -a: shows all contents including hidden ones of a specific folder, ex. ls -a python_decal_fa25
mkdir: creater a new folder, ex. mkdir newfolder
cat: shows the content of a file, ex. cat homework1.py would print the contents of this py file
pwd: print working directory, shows the full path to my current location, ex. pwd homework1
cd ..: cd .. would move up to the parent folder
cd .: remains in the current folder/does nothing
cd ~: navigate to user home folder
cp: copies files and folders, ex. cp file.txt copy.txt copies file.txt to copy.txt
mv: move or rename files/folders, ex. mv oldname.txt newname.txt renames file from oldname to newname
rm: removes files/folders, cannot be undone, ex. rm file.txt removes the file permanently
clear: clears all previous commands in the terminal
grep: search for text in files, ex. grep "word" finds lines containing the word "word"

Questions: 

1. 
find: search for files and directories
ex. find . -name "*.py" finds all python files in the current directory
curl: downloads file from the link provided
ex. curl -0 https://link.com/file.zip downloads the file
kill: kills (ends) the process, requires the process id
ex kill (ID): kills the process that the ID represents, may use when a process is running becomes unresponsive and you cannot exit normally

2. ls shows all contents of the directory except for ones hidden, ls -a shows all including the hidden ones
3. hidden file is a file or folder on the computer that is not displayed by default 
4. 
-l: long format listing, shows detailed file info including permission, owner, size, date
ex. ls -l shows all folders in current directory including the info above
-f: forces the removal of files, overriding the confirmation prompts
ex. rm -f
-i: prompts for confirmation before the action is done
ex. rm -i example.py prompts for the removal of example.py before actually doing so
"""









