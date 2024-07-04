
import Modules 
import Modules as mine
from Modules import person1

# Python Module:
'''
What is a Module?

Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.
'''

#Create a Module:
'''To create a module just save the code you want in a file with the file extension .py'''

def greeting(name):
  print("Hello, " + name)  
'''Save this code in a file named mymodule.py'''

#Use a Module:
'''Now we can use the module we just created, by using the import statement.'''

     #Import the module named mymodule, and call the greeting function:

Modules.greeting("Jonathan")

#variables in Module:
'''The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):
'''

Person1 = {
  "name": "Bhargav",
  "Age": "24",
  "city": "Naidupet"
}

a = Modules.Person1['name']
print(a)

a = mine.Person1
print(a)

#Built modules:
'''There are several built-in modules in Python, which you can import whenever you like.'''
       #Import and use the platform module:

import platform

x = platform.system()
print(x)

#Using the dir() function:
'''There is a built-in function to list all the function names (or variable names) in a module. The dir() function.'''
   #List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)
  #Note: The dir() function can be used on all modules, also the ones you create yourself.

#Import from the module:
'''You can choose to import only parts from a module, by using the from keyword.'''

  #The module named mymodule has one function and one dictionary:

'''def greeting(name):
      print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}


print (person1["age"])'''


#Note: When importing using the from keyword, do not use the module name when referring to elements in the module.
#  Example: person1["age"], not mymodule.person1["age"]

