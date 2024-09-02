################################################ Python Notes ####################################################

######## Python Comments ####### (28-08-2024)
""" 1.Comments can be used to explain Python code.
    2.Comments can be used to make code more readable.
"""

######## Python Variables #######
# Variable:
""" 1.Variables are containers for storing the data.
    2.Variable names must begin with a letter or an underscore, but they can be a group of both letters and digits.
"""
a =10
b = "Bhargav" # this is how we declare the variable
print(a)
print(b)

# Today

A=str(3)
c= float(2) # this is called casting
print(A)
print(c)

# *. Variable names are case-sensitive
 
 #### varaible Names ####
'''A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
*.A variable name must start with a letter or the underscore character
*.A variable name cannot start with a number
*.A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
*.Variable names are case-sensitive (age, Age and AGE are three different variables)
*.A variable name cannot be any of the Python keywords.'''

_Name="bhargav"
print(_Name)
var_Name=5
print(var_Name)
VARNUM=6
Var_Name3="Muni"
print(VARNUM)
print(Var_Name3)

#### Multi Words Varaibles Names ####
''' *.Variable names with more than one word can be difficult to read.
    *.There are several techniques you can use to make them more readable.
'''
# Camel Case:
'''Each word, except the first, starts with a capital letter.'''
  #example:
myVariableName = "Bhargav Nageti"

#Pascal Case:
'''Each word starts with a capital letter.'''
  #example:
MyVariableName = "John"

#Snake Case:
  #example:
my_variable_name = "MuniChandra"

#### Assign Multiple Values ####
# Many Values to Multiple Variables:
'''Python allows you to assign values to multiple variables in one line.'''
 #example:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Note: Make sure the number of variables matches the number of values, or else you will get an error.

# One Value to Multiple Variables:
'''And you can assign the same value to multiple variables in one line.'''
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection:
'''If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.'''
 #Example:
 #Unpacking List:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)