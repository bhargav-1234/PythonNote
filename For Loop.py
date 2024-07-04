# Python For Loop:

#For loop:
'''
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

'''

fruits = ["banana", "mango", "grape"]
for x in fruits:
    print(x)

    #The for loop does not require an indexing variable to set beforehand.

# Looping through a String:
'''Even strings are iterable objects, they contain a sequence of characters.'''

for x in "banana":
    print(x)

#The Break Statement:
'''With the break statement we can stop the loop before it has looped through all the items.'''

fruits = ["mango", "banana", "grape", "orange", "kiwi"]
for x in "grape":
    print(x)
    if x == "grape":
      break


cars = ["suzuki", "tesla", "bmw", "Audi"]
for x in cars:
    if x == "bmw":
        break
    print(x) 


#Continue statement:
'''With the continue statement we can stop the current iteration of the loop, and continue with the next.'''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


  # range() Function:
  '''
  To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
and ends at a specified number.
  '''

for x in range(10):
     print(x)

for x in range(2, 10):
   print(x)

for x in range(5, 10, 2):
   print(x)


#else in for-loop:
'''The else keyword in a for loop specifies a block of code to be executed when the loop is finished.'''

for x in range(6):
   print(x)
else:
   print('successfully completed')

for x in range(6):
   if x == 3: break
   print(x)
else:                #If the loop breaks, the else block is not executed.
   print('successfully completed')


#Nested loop:
'''
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop"
'''
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# The Pass Statement:
'''for loops cannot be empty, but if you for some reason have a for loop with no content, 
put in the pass statement to avoid getting an error.'''

for x in [0, 1, 2]:
  pass

# having an empty for loop like this, would raise an error without the pass statement
