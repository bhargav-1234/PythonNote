import datetime
import json
import random
import sys
a = 12
try:
    print(a)
except:
    print("Something went wrong")
    
print(json.dumps(["mango", "orange", "grape"]))
x = datetime.datetime.now() # it prints present local time
print(x)
X = 300  #Global variable
def my_function():
    X = 100  #local variable
    print(X)
my_function()
print(X)
# Global keyword
def fun():
   global b # by using "global" keyword we can use it anywhere in the function
   b = "Bhargav"
   print(b)
fun()
print(b)
############"Data Types"###########
"""Text Type:	str
   Numeric Types:	int, float, complex
   Sequence Types:	list, tuple, range
   Mapping Type:	dict
   Set Types:	set, frozenset
   Boolean Type:	bool
   Binary Types:	bytes, bytearray, memoryview
   None Type:	NoneType"""

c = "Bhargav"  #str data type
print(c)
c = 2    # int data type
print(c)
c = 5.2   #float data type
print(c)
c = ["mango", "orange", "dragon", "water melon", "grape"] #list data type
print(c)
c = ("mango", "orange", "dragon", "water melon", "grape") #tuple data type
print(c)
c = {"name":"Harika", "age":16} # dict data type
print(c)
c = {"banana", "Bhargav", "Harika"} #set data type
print(c)
c = True #boolean data type
print(c)
c = b"Hello" #byte data type
print(c)
c = bytearray(5) # byte data type
print(c)
c = memoryview(bytes(5)) #byte data type
print(c)
c = None #None data type
print(c)
c = range(2)
print(c)

################"Numbers"#################
# There are three types of Python Numbers, they are:
#       1.int
#       2.float
#       3.complex

x = 1    #int
y = 2.5  #float
z = 1j   #complex
print(x)
print(y)
print(z)

# You can convert from one type to another with the int(), float(), and complex() methods:

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

# Random Number
"""Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used to make random numbers:
"""

print(random.randrange(1, 100))

######################"Python Casting"######################

# Specify a Variable Type
"""There may be times when you want to specify a type on to a variable. This can be done with casting. 
Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), 
or a string literal (providing the string represents a whole number)

float() - constructs a float number from an integer literal, a float literal or 
a string literal (providing the string represents a float or an integer)

str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""

x = int(1)
y = int(2.5)
z = int("5")

print(x)
print(y)
print(z)

x = float(1)
y = float(2.5)
z = float("5.1")

print(x)
print(y)
print(z)

x = str(1)
y = str(2.25)
z = str("Bhargav")

print(x)
print(y)
print(z)
print(random.randint(1,20))
#print("hello, my name is ", sys.argv[1])
def main():

    print("hi there how are you ")
main()

#List Comprehension


Person = ["Piyali", "Hiya", "Rudrashish", "Badsha", "Lipi"]  
newlist = [x for x in Person if "R" in x]  
print(newlist)  

numbers = [6,5,7,15]
num =[]
for n in numbers:
    num.append(n**2)
print(num)

number = [6,5,7,15]
num = [n**2 for n in number]
print(num)

####
# Import module to keep track of time  
import time  
   
# defining function to execute for loop  
def for_loop(num):  
    l = []  
    for i in range(num):  
        l.append(i + 10)  
    return l  
   
# defining function to execute list comprehension  
def list_comprehension(num):  
    return [i + 10 for i in range(num)]  
   
# Giving values to the functions  
   
# Calculating time taken by for loop  
start = time.time()  
for_loop(10000000)  
end = time.time()  
  
print('Time taken by for loop:', (end - start))  
   
# Calculating time taken by list comprehension  
start = time.time()  
list_comprehension(10000000)  
end = time.time()  
  
print('Time taken by list comprehension:', (end - start))  

#######
# Using List Comprehension to Iterate through String
letters = [ alpha for alpha in 'javatpoint' ]  
print( letters)  

####
# Using Conditions in List Comprehension
number_list = [ num for num in range(30) if num % 2 != 0]  
print(number_list)  


# Addition of odd elements to the List:

def Sum(n):  
    dsum = 0  
    for ele in str(n):  
        dsum += int(ele)  
    return dsum  
List = [23, 69, 73, 97, 105, 845, 307]  
newList = [Sum(i) for i in List if i & 1]  
print(newList)  