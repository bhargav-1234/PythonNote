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

# Output Variables:
'''The Python print() function is often used to output variables.'''
 #example:
x = "Python is awesome"
print(x)
    
#In the print() function, you output multiple variables, separated by a comma:

 #Example:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:
 #example:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

        #example:
        # a =10
        # b ="Bhargav" /* It gives an error because we are adding the sting and integer value 
        # print(a + b)

# Global Variables:
'''Variables that are created outside of a function are known as global variables.
   Global variables can be used by everyone, both inside of functions and outside.'''
 # Example:
x =10  # This is global variable

def Global():
    print(x + 10)
Global()

'''If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
   The global variable with the same name will remain as it was, global and with the original value.'''

 #Example:
x= 5

def fun():
    x ="Awesome"
    print("Python is "+ x)
fun()
print(x)

# Global Keyword:
'''Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
   To create a global variable inside a function, you can use the global keyword.'''
  # Exmaple:
def my_Fun():
   global z
   z ="Bhargav"
   
my_Fun()
print("Hello, " + z + " hope you having great time with your family")

######### Python Data Type #########

## Built-in Data Type ##
''' *.In programming, data type is an important concept.
    *.Variables can store data of different types, and different types can do different things.
    *.Python has the following data types built-in by default, in these categories'''

'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''
#getting the data type
''' we can get data type of any object by using the "type()" function. '''

 #example:
# x= 5
# print(type(x))

# Setting the data type:
'''x = "Hello World"	                         str	
x = 20	                                       int	
x = 20.5	                                     float	
x = 1j	                                       complex	
x = ["apple", "banana", "cherry"]	             list	
x = ("apple", "banana", "cherry")	             tuple	
x = range(6)	                                 range	
x = {"name" : "John", "age" : 36}	             dict	
x = {"apple", "banana", "cherry"}	             set	
x = frozenset({"apple", "banana", "cherry"})	 frozenset	
x = True	                                     bool	
x = b"Hello"	                                 bytes	
x = bytearray(5)	                             bytearray	
x = memoryview(bytes(5))	                     memoryview	
x = None	                                     NoneType'''

# Python Numbers
'''There are three numeric types in Python:
1.int
2.float
3.complex  '''
#Example:
x =5
y =1.25
z=1+5j 
print(type(x))
print(type(y))
print(type(z))

# Type Conversion
'''You can convert from one type to another with the int(), float(), and complex() methods.'''
 
 #example:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
# Note: You cannot convert complex numbers into another number type.

### Random Number ###
'''Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used to make random numbers'''

#example:
import random

print(random.randrange(1, 10))