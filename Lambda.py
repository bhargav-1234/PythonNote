# Pytho,m LAmbda:
'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
'''
  #Syntax: lambda arguments : expression


x = lambda a : a + 10
print(x(5))    #Lambda functions can take any number of arguments


x = lambda a : a * 5
print(x(2))

a = lambda x, y : x * y
print(a(4, 2))

x = lambda a ,b, c : a + b + c
print(x(4, 2 , 5))

#Why using lambda functions:
'''The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number.
'''

       #def myfunc(n):
       #return lambda a : a * n
'''Use that function definition to make a function that always doubles the number you send in.'''

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
############
def my_function(n):
  return lambda a : a * n

mydoubler = my_function(5)

print(mydoubler(8))
############
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

