#########################"Python Lists"############################
#List:
'''
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, 
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets
'''

thislist = ["Bhargav", "Arun", "MuniChandra", "Nagalakshmi"]
print(thislist)

   #List items:
'''
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.
'''

  #Ordered:
'''
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.
'''

#Changeable:
'''The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.'''

#Allow Duplicates:
'''Since lists are indexed, lists can have items with the same value'''

list = ["apple", "mango", "banana", "orange", "apple", "grape"]
print(list)

#List length:
'''To determine how many items a list has, use the len() function'''

list = ["apple", "banana", "grape", "mango"]
print(len(list))

#List Items - Data Types:
'''List items can be of any data type'''

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

'''A list can contain different data types'''

list1 = ["abc", 34, True, 40, "male"]

print(list1)


#type():
'''From Python's perspective, lists are defined as objects with the data type 'list' '''
   # <class 'list1'>

list = ["Bhargav", "arun", "munichandra", "Srikanth"]
print(type(list))

#Python Collections (Arrays):
'''
There are four collection data types in the Python programming language:

List - is a collection which is ordered and changeable. Allows duplicate members.
Tuple - is a collection which is ordered and unchangeable. Allows duplicate members.
Set - is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary - is a collection which is ordered** and changeable. No duplicate members.
'''


#Access the list items:
'''List items are indexed and you can access them by referring to the index number'''

names = ["Bhargav", "Arun", "Munichandra", "Srikanth", "Nagalakshmi"]
print(names[1])

#Negetive indexing:
'''
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.
'''

names = ["bhargav", "muni" , "naga", "sri", "arun"]
print(names[-2])

#range of index:
'''
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.
'''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

    #This will return the items from position 2 to 5.

    #Remember that the first item is position 0,
    #and note that the item in position 5 is NOT included

print(thislist[:4])
print(thislist[2:])
print(thislist[-5:-2])
if "kiwi" in thislist:
    print('yes, it is')

#Change list items:
'''To change the value of a specific item, refer to the index number'''

thislist[1] = "Dragon fruit"
print(thislist)

thislist[1:2] = ["blacukcurrant", "watermelon"]
print(thislist)

mylist = ["apple", "banana", "watermelon"]
mylist[1:3] = ["grape"]
print(mylist)

#Insert items:
'''
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index
'''

mylist = ["apple", "mango", "watermelon"]
mylist.insert(2, "grape")
print(mylist)

#Add list items:
'''To add an item to the end of the list, use the append() method'''

   #Using the append() method to append an item 

mylist.append("orange")
print(mylist)

#Extend list:
'''To append elements from another list to the current list, use the extend() method.'''

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add Any Iterable:
'''The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).'''

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove lists:
'''The remove() method removes the specified item.'''

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

'''The pop() method removes the specified index.'''

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

'''If you do not specify the index, the pop() method removes the last item.'''

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

'''The del keyword also removes the specified index.'''

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

'''The del keyword can also delete the list completely.'''
   #del thislist

#Clear the list:
'''The clear() method empties the list.

The list still remains, but it has no content.'''

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


   #Loop lists:
'''You can loop through the list items by using a for loop'''

mylist = ["Bhargav", "Muni", "naga", "Arun", "Srikanth"]
for x in mylist:
    print(x)

'''
You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.
'''

names = ["mango", "banana", "orange", "grape"]
for i in range(len(names)):
    print(names[i]) 

   #using while loop:
'''
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration.
'''

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

    #Looping Using List Comprehension:
'''List Comprehension offers the shortest syntax for looping through lists'''

thislist = ["bhargav", "orange", "banana", "watermelon"]
[print(x) for x in thislist]


#list comprehension:
'''
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside
'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
##########
flowers = ["rose", "lavendor", "jasmine", "white rose"]
newlist = []

for x in flowers:
   if "j" in x:
      newlist.append(x)
print(newlist)
#######
newlist = [x for x in flowers if "v" in x]
print(newlist)

   #Iterable:
'''The iterable can be any iterable object, like a list, tuple, set etc.'''
       #You can use the range() function to create an iterable:

newlist = [x for x in range(10)]

print(newlist)


   #Expresion:
'''
The expression is the current item in the iteration, but it is also the outcome, 
which you can manipulate before it ends up like a list item in the new list:

'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)
######
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

#Sort list:

  #Sort List Alphanumerically:
'''List objects have a sort() method that will sort the list alphanumerically, ascending, by default.'''

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)
####
thislist = [100, 50, 65, 82, 23]

thislist.sort()

print(thislist)

  #Sort Descending:
'''To sort descending, use the keyword argument reverse = True.'''

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#####
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

   #Customize Sort Function:
'''
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first
'''

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)

   #Case Insensitive sort:
'''By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters.'''

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort()

print(thislist)
####
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

  #Reverse Order:
'''
What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements.
'''

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#####
thislist = ["bhargav", "arun", "muni", "sri", 'naga']
thislist.reverse()
print(thislist)

#Copy list:
'''
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1,
 and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy().
'''

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

   #Another way to make a copy is to use the built-in method list().

#Join list:
'''
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.
'''
num1 = [1, 2, 4]
num2 = [6, 5, 8]
print(num1 + num2)
#####
name = ["bhargav", "arun", "naga", "muni"]
num = [5, 3 , 4 , 8]
total = name + num
print(total)
#####
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
   #Or you can use the extend() method, which purpose is to add elements from one list to another list:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)