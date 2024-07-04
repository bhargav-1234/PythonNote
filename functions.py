#Python Fuctions:
'''
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

'''

#Creating Function:
'''In Python a function is defined using the def keyword.'''

def my_function():
    print('my first function')

my_function()


#Arguments:
'''
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, 
just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, 
which is used inside the function to print the full name

'''

def my(fname):
    print(fname + " Nageti")

my("Bhargav")
my("Harika")
my("muni")

# Parameters Or Arguments:
'''
The terms parameter and argument can be used for the same thing: information that are passed into a function.
'''
# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.


# Number of Arguments:
'''
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, 
you have to call the function with 2 arguments, not more, and not less.

'''

def my_fun(fname, lname):
    print(fname + " " + lname)
my_fun("Bhargav", "Nageti")


#Arbitrary Arguments, *args :
'''
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly
'''

def my_function(*kids):
    print("My Eldest Brother is: " + kids[1])
my_function("Bhargav", "Muni Chandra", "Arun")


# Keyword Arguments:
'''
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.
'''

def my_function(child1, child2, child3):
    print("my name is: " + child1)
my_function("Bhrgav", "muni", "arun")


# Arbitrary Keyword Arguments, **kwargs:
'''
If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly
'''

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


#Default Parameter Value:
'''If we call the function without argument, it uses the default value.
'''

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def hello(city = "Naidupet"):
    print("I am from " + city)


hello("Nellore")
hello("kalahasti")
hello()
hello('tirupati')

#Passing a List as an Argument:
'''You can send any data types of argument to a function (string, number, list, dictionary etc.), 
and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function.
'''

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)



def my_function(names):
   for x in names:
      print(x)

names = ["Bhargav", "Muni Chandra", "Nagalakshmi",]
my_function(names)


# return value:
'''To let a function return a value, use the return statement.
'''

def math(x):
  return 5 * x
print(math(5))
print(math(2))
print(math(8))


#Recursion:
'''
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. 
This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, 
or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and 
mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, 
which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
'''


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)