#Python Arrays:
'''Arrays are used to store multiple values in one single variable.'''
  #Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

car = ["Bmw", "Volvo", "Suzuki", "Benz"]
print(car)

#What is an Array:
'''
An array is a special variable, which can hold more than one value at a time.

If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?

The solution is an array!

An array can hold many values under a single name, and you can access the values by referring to an index number.
'''

#Access the Elements of an Array:
'''You refer to an array element by referring to the index number.'''

fruits = ['mango', "water melon", 'grape', 'banana']
x = fruits[2]
print(x)
##########
fruits = ['Dragon fruit', 'apple', 'banana', 'cherry']
fruits[1] = "mango"
print(fruits)
########
name = ['Bhargav', "Muni chandra", 'Nagalakshmi', "sri"]
a = len(name)
print(a)
#########
for y in name:
    print(y)

############
name.append('Arun')
print(name)
###########
name.pop(3)
print(name)
##########
name.remove("Bhargav")
print(name)