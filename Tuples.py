#Tuples:

'''
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
'''

mytuple = ("bhargav", "muni", "arun", "naga")
print(mytuple)

   #Tuple Items:
'''
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
'''

   #Ordered:
'''When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.'''

   #Unchangable:
'''Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.'''

   #Allow Duplicates:
'''Since tuples are indexed, they can have items with the same value.'''

my_tuple = ('banana', 'orange', 'mango', 'grape', 'banana')
print(my_tuple)
######
thistuple = ("watermelon", "banana", "cherry", "apple", "cherry")
print(thistuple)


#Tuple length:
'''To determine how many items a tuple has, use the len() function'''

tuple = ('cherry', 'banana', 'grape', 'apple')
print(len(tuple))

  #Create Tuple With One Item:
'''To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
'''

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

  #Tuple items can be of any data type:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

#type():
'''From Python's perspective, tuples are defined as objects with the data type 'tuple'''

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#Acces tuple item:
'''You can access tuple items by referring to the index number, inside square brackets'''
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negitive indexing:
'''Negative indexing means start from the end.
-1 refers to the last item, -2 refers to the second last item etc.
'''

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#range of indexing:
'''You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items.
'''

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
######
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
######
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#Check if item exists;
'''To determine if a specified item is present in a tuple use the in keyword.'''

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Update tuple:
'''Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

But there are some workarounds.
'''

    #Change the tuple value:
'''Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.'''

#Example:
'''x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)'''

#add items:
'''Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, 
add your item(s), and convert it back into a tuple.'''

      #thistuple = ("apple", "banana", "cherry")
         #y = list(thistuple)
         #y.append("orange")
         #thistuple = tuple(y)

         #print(thistuple)

#2. Add tuple to a tuple: 
'''You are allowed to add tuples to tuples, 
so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple'''

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Remove items:
'''Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items'''


      #thistuple = ("apple", "banana", "cherry")
      # y = list(thistuple)
      #y.remove("apple")
      #thistuple = tuple(y)

'''The del keyword can delete the tuple completely'''

    #thistuple = ("apple", "banana", "cherry")
    #del thistuple
    #print(thistuple) #this will raise an error because the tuple no longer exists    


#Unpack Tuple:
'''When we create a tuple, we normally assign values to it. This is called "packing" a tuple.'''

fruits = ("apple", "banana", "cherry")

print(fruits)

'''But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking".'''

fruits = ("mango", "grape", "watermelon")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
     #Note: The number of variables must match the number of values in the tuple, 
     # if not, you must use an asterisk to collect the remaining values as a list.


#Using Asterisk*
'''If the number of variables is less than the number of values, 
you can add an " * "to the variable name and the values will be assigned to the variable as a list.'''

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

'''
If the asterisk is added to another variable name than the last, 
Python will assign values to the variable until the number of values left matches the number of variables left.
'''

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

colours = ("red", "black", "blue", "pink", "yellow", "green")
(apple, *banana, grape) = colours

print(apple)
print(banana)
print(grape)


#Loop Tuple:
'''You can loop through the tuple items by using a for loop.'''

thistuple = ("bhargav", "muni", "naga")
for x in thistuple:
  print(x)

'''
You can also loop through the tuple items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.
'''

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Using While Loop:
'''
You can loop through the tuple items by using a while loop.

Use the len() function to determine the length of the tuple, then start at 0 and loop your way through 
the tuple items by referring to their indexes.

Remember to increase the index by 1 after each iteration.
''' 

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

cars = ("benz", "Tata", "Suzuki", "Innova")
i = 0
while i< len(cars):
  print(cars[i])
  i = i+1

#Join Tuple;
'''To join two or more tuples you can use the + operator.'''

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

Person = ("Bhargav", "nagalakshmi", "Muni Chandra", "Arun")
numbers = (1 , 2 , 3 , 5)
print(Person + numbers)

#Multiply Tuples:
'''If you want to multiply the content of a tuple a given number of times, you can use the * operator.'''

my_tuple = Person * 2
print(my_tuple)


#tuple methods:
'''Python has two built-in methods that you can use on tuples.'''
      #count()
      #index()

#count():
'''The count() method returns the number of times a specified value appears in the tuple.'''

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)   #Syntax:tuple.count(value)

print(x)

#index():
'''
The index() method finds the first occurrence of the specified value.

The index() method raises an exception if the value is not found.
'''

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)   #Syntax:tuple.index(value)

print(x)

