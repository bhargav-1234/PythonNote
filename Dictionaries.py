###################"Dictionaries"##################

import json
#Dictionary;
'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

   thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

Dictionaries are written with curly brackets, and have keys and values.

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


#Dictionary Items:
'''
Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


my_dict = {
    "name": "Bhargav",
    "wife": "Harika",
    "city": "Naidupet",
    "District": "Tirupati"

}

print(my_dict)
print(my_dict['wife'])


#Ordered or Unordered:
'''
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items does not have a defined order, you cannot refer to an item by using an index
'''

#Changable:
'''Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.'''

     #Dictionaries cannot have two items with the same key.

          #Example;
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict))

#Dictionary items -Data type:
'''The values in dictionary items can be of any data type.'''

thisdict = {
    1:{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
    },
    2:{
    "name": "Bhargav",
    "honey": "Harika",
    "Marriage date": "Future",
    "Childrens": 2
    }
}

print(thisdict)
#######

#dict() constructor:
thisdict = dict(name = "bhargav", age = 23, colour = "white")
print(thisdict)

#Access Dictionary items:
'''You can access the items of a dictionary by referring to its key name, inside square brackets.'''

details= {
    'name': 'bhargav',
    "qualification": "B.tech",
    'year': '2019',
    "job": "Software Engineer",
    "company": "Capgemini"
}

print(details["job"])

      #There is also a method called 'get()' that will give you the same result:

print(details.get('company'))


#Get keys:
'''The keys() method will return a list of all the keys in the dictionary.'''

print(details.keys())

  #The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
print(car)


#Get Values:
'''The values() method will return a list of all the values in the dictionary.'''

my_details = {
    'name': "Bhargav",
    "city": "Naidupet",
    "Education": "B.tech",
    "year": "2019",
    "moble no": 9550547019

    }

print(my_details.values()) #before change

my_details['friend'] = 'harika'
print(my_details.values())  #after Change

#Get items:
'''The items() method will return each item in a dictionary, as tuples in a list.'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)

if 'model'in thisdict:
    print('YES')


#Change dictionary items:

#Change values:
'''You can change the value of a specific item by referring to its key name.'''

hello = {
    "name": "harika",
    'age': 16,
    'color': "white",
    "education": "10th (pursuing)"

}
hello["name"] = 'Harika + Bhargav'
print(hello)

#upadte Dictionary:
'''The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.
'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "name": "Harika"
}
thisdict.update({"year": 2020})
thisdict.update({'name':"Bhargav"})
print(thisdict)

#Add Dictionary items:

#Add values:
'''Adding an item to the dictionary is done by using a new index key and assigning a value to it.'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


#removing Dictionary items:

#Removing item:
'''There are several methods to remove items from a dictionary.'''

cars = {
    "name": 'Benz',
    "color": "Black",
    "price": 2000000,
    "Model": 2023,
    'milage': "100km"
    }
cars.pop('Model')
#print(cars.pop("Model"))
print(cars)

  #The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

   #The del keyword removes the item with the specified key name

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

   #The del keyword can also delete the dictionary completely:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#del thisdict
print(thisdict)

 #The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#Looop dictionary:
'''
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
'''

Person_details ={
    "name": "Bhargav",
    "age": 24,
    "Blood Group": "B+",
    "city": "Naidupet",
    'Education': "B.Tech"
    
}

for x in Person_details:
    print(Person_details[x]) # it gives the values
    print(x) # it gives only keys

#You can also use the values() method to return values of a dictionary:

for x in Person_details.values():
    print(x)

#You can use the keys() method to return the keys of a dictionary:

for x in Person_details.keys():
    print(x)

#Loop through both keys and values, by using the items() method:

for x, y in Person_details.items():
    print(x, y)


#Copy Dictionaries:

#Copy Dictionary:
'''
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, 
and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy()
'''

my_view = {
    "name": 'Harika',
    'age': 17,
    "city": "Naidupet",
    'Blood Group': "B+"
}

details = my_view.copy()
print(details)

#Another way to make a copy is to use the built-in function dict().

never = dict(my_view)
print(never)

#Nested Dictionaries:
'''A dictionary can contain dictionaries, this is called nested dictionaries.'''

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#print(myfamily,)
print(json.dumps(myfamily, indent=4))

####
child1 = {
  "name" : "Bhargav",
  "year" : 2004
}
child2 = {
  "name" : "Sri",
  "year" : 2007
}
child3 = {
  "name" : "Arun",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(json.dumps(myfamily, indent=4))

# Access item in Nested DIctionaries:
'''To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary.'''

Details = {
"Child1": {
    "name": "Bhargav",
    "age": "24"
},
"Child2":{
    "name": "Srikanth",
    "age": 27
},
"Child3":{
    "name": "MuniChandra",
    'age': "32"
},
"Child4":{
    "name": "Nagalakshmi",
    'age': "29"
}
    
}
print(Details["Child3"]["name"])

#################
students = {
    "harry": "Griffindor",
    "draco": "slytherin",
    "luna": "hufulpuf",
    "ron": "grifindor"
}
 
for student in students:
      print(student, students[student], sep=" :")

