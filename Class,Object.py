#Python Classes and Objects;
'''
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
'''

#Create a Class:
'''To create a class, use the keyword class'''
class hello:
    print("hi there")

#create an Object:
'''Now we can use the class named MyClass to create objects'''
class my_class:
    x = 5

p1 = my_class()
print(p1.x)

#The __init__() Function;
'''
To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do 
when the object is being created
'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(p1.name, p1.age)
###############
class Name:
   def __init__(self, fname, age):
      self.fname = fname
      self.age = age

x = Name("Bhargav", 24)

print(x.fname)
print(x.age)

   #Note: The __init__() function is called automatically every time the class is being used to create a new object.


#The __str__() Function:
'''
The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned.
'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

#Object Method:
'''Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

   #Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

class Details:
   def __init__(self, name, age):
      self.name = name
      self.age = age
   
   def info(self):
      print("hello my name is " + self.name)
x1 = Details("bhargav",24)
x1.info()


#Modify Object Properties:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)

#delete the object;
'''You can delete properties on objects by using the del keyword'''

#class Person:
  #def __init__(self, name, age):
    #self.name = name
    #self.age = age

  #def myfunc(self):
    #print("Hello my name is " + self.name)

#p1 = Person("John", 36)

#del p1.age
#print(p1.age)

#delete object:
'''You can delete objects by using the del keyword.'''
     
'''class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1)'''


#The Pass Statement:
'''

class definitions cannot be empty, but if you for some reason have a class definition with no content, 
put in the pass statement to avoid getting an error.

'''

class Person:
  pass

