#############################"Boolean"###############################
#Boolean:
'''Booleans represent one of two values: True or False.'''

#Boolean Values:
'''
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer
'''

print(12 >  2)
print(3 < 1)
print(4 == 2)


'''When you run a condition in an if statement, Python returns True or False:'''

a = 100
b = 200
if a > b :
    print("Yes a is greater than b")
else:
    print("No a is not greater than b")

   # Evaluate Values and Variables:
'''The bool() function allows you to evaluate any value, and give you True or False in return,'''

print(bool("Bhargav"))
print(bool(15))


'''One more value, or object in this case, evaluates to False, 
and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
'''

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

'''Functions can return boolean value'''

def my_function():
   return True
   
print(my_function())
#####

def my():
   return False

if my():
   print("yes")

else:
   print("No")


"""Python also has many built-in functions that return a boolean value, like the isinstance() function, 
which can be used to determine if an object is of a certain data type:"""

x = 100
print(isinstance(x, int))

t1=(1,2,4,3)
t2=(1,2,3,4)
print(t1 < t2)