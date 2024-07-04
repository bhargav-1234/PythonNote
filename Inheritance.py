# Python Inheritance:
'''
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

'''

#Create Parent Class:
'''Any class can be a parent class, so the syntax is the same as creating any other class.'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
########################
class Details:
  def __init__(self, name, age, number):
    self.name = name
    self.age = age
    self.number = number
  
  def printname(self):
    print(self.name, self.age, self.number)

x = Details("Bhargav", 24, 9550547019)
x.printname()
############
class Number:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Number("Bhargav", "Nageti")
x.printname()

#Create Child Class:
'''To create a class that inherits the functionality from another class, 
send the parent class as a parameter when creating the child class.'''

       #Create a class named Student, which will inherit the properties and methods from the Person class:

                        #class Student(Person):
                         #pass

            #Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

class Student(Person):
  pass

x = Student("Bhargav", "muni")
x.printname()


# Add the __init__() Function:
'''
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Note: The __init__() function is called automatically every time the class is being used to create a new object.
'''

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Harika", "Nageti")
x.printname()

#Use the Super() Function:
'''Python also has a super() function that will make the child class inherit all the methods and properties from its parent.'''

class Student(Person):
  def __init__(slef, fname, lname):
    super().__init__(fname, lname)

x = Student("Nagalakshmi", "nageti")
x.printname()
   #By using the super() function, you do not have to use the name of the parent element, 
   # it will automatically inherit the methods and properties from its parent.          

#Add properties:
class Person:
  def __init__(self, fname, lname, year):
    self.fname = fname
    self.lname = lname
    #self.year = year

  def printname(self):
    print(self.fname, self.lname, self.year)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname, year)
    self.year = 2023

x = Student("Bhargav", "Nageti", 2023)
x.printname()

##############
class Parent:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  def printname(self):
    print(self.fname, self.lname)

class Child(Parent):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)

x = Child("Muni", "Nageti", 2019)
x.welcome()
############
class Father:
  def __init__(self, fname,lname, year ):
    self.fname = fname
    self.lname = lname
    self.year = year

  def printname(self):
    print(self.fname, self.lname, self.year)

class Child(Father):
  pass

  def welcome(self):
    #def __init(self, fname, lname, year):
      #self.year = 2019

      print("welcome", self.fname, self.lname, "to our company in the year of", self.year)

x = Child("Arun", "nageti", 2019)
x.welcome()
