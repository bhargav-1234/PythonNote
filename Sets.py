###############################"Python Sets"#################################

#Sets:
'''
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, 
all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.
'''

thisset = {'bhargav', 'harika', 'Aruna', 'Vinay'}
print(thisset)

#Set items:
'''Set items are unordered, unchangeable, and do not allow duplicate values.'''

#Unordered:
'''
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

'''

#Unchangable:
'''
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

'''

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#Get the Length of a Set
#To determine how many items a set has, use the len() function.

thisset = {"apple", "banana", "cherry"}

print(len(thisset)) 

#Set items - Data Types:
'''Set items can be of any data type.'''

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

   #A set can contain different data types:

set = {"bhargav", 5, "harika", True, 45}
print(set)


#The Set() Constructor:
'''It is also possible to use the set() constructor to make a set.'''

#thisset = set(("apple", "banana", "cherry"))
#print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.


#Access items:
'''
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
'''

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
######
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


#Add Set Items:
'''
Once a set is created, you cannot change its items, but you can add new items.

To add one item to a set use the add() method.
'''

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Add Set:
'''To add items from another set into the current set, use the update() method.'''

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


#Add any Iterable:
'''The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
'''

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


#Remove Set Items:
'''To remove an item in a set, use the remove(), or the discard() method.'''

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

    #Remove "banana" by using the discard() method.

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

    #You can also use the pop() method to remove an item, but this method will remove a random item, 
    # so you cannot be sure what item that gets removed.

    #The return value of the pop() method is the removed item.

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

    #The clear() method empties the set


thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


   #The del keyword will delete the set completely:

          #thisset = {"apple", "banana", "cherry"}

          #del thisset

          #print(thisset)


#Loop Sets:
'''You can loop through the set items by using a for loop'''

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#Join Sets:

#join two sets:
'''
There are several ways to join two or more sets in Python.

You can use the union() method that returns a new set containing all items from both sets,
 or the update() method that inserts all the items from one set into another
'''

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


#The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
    #Note: Both union() and update() will exclude any duplicate items.


#The intersection_update() method will keep only the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)


#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates.

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)
print(z)

