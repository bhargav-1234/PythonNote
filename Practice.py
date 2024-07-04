"""import sys

print("Hello Bhargav")
a = 4
b = 8
z = a+b
print(z)
if (a<b):
    print("a is less than b")

else:
    print("b is greater than a ")
print(sys.version)


x = 5
y = "Hi Bhargav"
c = float(5)
#print(x+y)
# These are called comments
print("Hi Honey")
print(x)
print(y)
print(c)

X = int(5)
Y = str("4")
Z = float(2)
print(X)
print(Y)
print(Z)
print(type(x))
print(type(y))
n = 'Bhargav'
print(n)
myname = "Bhargav"
my_name = "Honey"
_my_name = "bhargav"
MyName = "honey"
myName = "i love you"
myFirstName = "Bhargav"""

print("Hello Bhargav")
myLastName = "Honey"
MyFirstName = "Bhargav"
print(MyFirstName)
print(myLastName)
My_First_Name = "honey"
print(My_First_Name)
x,y,z = "Mango","orange","Grape"
print(x)
print(y)
print(z)
a=b=c ="Lemon"
print(a)
print(b)
print(c)
fruits=["watermelon","Karbuja","apple"]
X,Y,Z = fruits
print(X)
print(Y)
print(Z)
x1 = "hello Honey"
print(x1)
x2 = "hello"
x3= "Bhargav"
x4="Honey"
print(x2,x3,x4)
print(x2 + x3 + x4)
x= "Awesome"
def myfun():
    x = "fantastic"
    print("Python is:" +x)
  
myfun()
print("python is" +x)

"""Global Variable"""
def my():
    global s
    s ="Superb"
my()
print("Bhargav is "+s)

"""Data Types"""
a=25
def cal():
    a =10 
    b = 45
    print(a+b)
cal()
print(a)

a=55 #int
b="Bhargav" #String
c=2.2 #float
d = 2j #Complex
x= {"name":"Bhargav","age":25} #Dictionary
y = ["Red","Black","White"] #list
z =("mirror","lap","love")
######### Numbers ##########
x5= 12
x6 = 2.5
x7 = 1+2j

a1 = complex(x6)
a2 = float(x5)
a3= int(x6)
print(a1)
print(a2)
print(a3)
### random Numbers ###
import random
print(random.randrange(0,10))

###### Strings ##########
name = "Bhargav"
Name ='Honey'     
print(name)
print(Name)
print("it's alright")
print("'Honey' is the best")
## MultiLine String ##
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
 
a="Honey"
print(a)

### Strings Are Arrays ##

a="Hello, World!"
print(a[1])
print(len(a))

for x in "Honey":
    print(x)

## checking the String ##
txt= "hello Honey how are you "
print("Honey" in txt)
if "Honey" in txt:
    print("yes there is")

## Slicing ##
p = "Hello,Bhargav"
print(p[4:9])
print(p[:6])
print(p[5:])
print(p[-5:-1])

## Modify Strings ##
a = "hello"
print(a.upper())
b  =" hello, world "
print(b.strip())
print(b.replace("h","H"))
print(b.split(","))

## String Concatenation ##
a= "Bhargav"
b = "Honey"
c = a + b
print(c)
print(a + "" + b)
age = 25
txt = f"Hi good evening iam bhargav and iam {age} years old "
print(txt)
price = 15
txt =f"The actual price of one cup tea is {15*45}"
print(txt)
txt = "There is only one man the in world whose stronger than all and he name is \"Bhargav\" "
print(txt)

#### String Methods ####
c = "honey"
print(c.capitalize())
print(c.casefold())

txt = "Honey"
x = txt.center(20)
print(x)

### Booleans ###

a=100
b=85
if(a<b):
    print("Incorrect")

else:
    print("No, a is greater than b")

print(bool("Bhargav"))
print(bool(15))
print(bool(""))
print(bool(0))
print(bool([]))
print(bool({}))
print(bool(["Bhargav","Honey","munichandra","nagalakshmi"]))

def myFunction():
    return False

print(myFunction())

def my():
    return True

if my():
    print("Yes")
else:
    print("No")
###########
class myclass():
  def __len__(self):
    return True

myobj = myclass()
print(bool(myobj))

##########
def myfunc():
    return True
print(myfunc())
###########
x = 200
print(isinstance(x, int))

### Operators ###
x =100
y=45
print(x + y)

#Artimetic Operator#

x=12
y=13
print(x - y)
print(x/y)
print(x*y)
print(x%y)
print(x**y)
print(x//y)

#Assignment Operators#
x =5
x+=3
print(x)
x-=3
print(x)
x/=3
print(x)
x*=3
print(x)
x//=3
print(x)
x**=3
print(x)
x=10
x|=3
print(x)
x^=3
print(x)
x>>=3
print(x)
x<<=3
print(x)
print(x:=3)

#Comparision Operators#
x = 10
y = 5
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x<<y)
print(x>>y)
print(x<=y)
print(x>=y)

## Logical Operators ##
a= 4
b =6
print(a<b and a>b)
print(a<b or a>b)
print(not(a<b and a>b))

## Identity Operators ##
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(y is z)
print(x is not z)
print(x is not y)
print(y is not z)
print("banana" in x)
print("mango" in x)
print("mango" not in x)

## Bit wise operator ##
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~3)
print(6 << 2)
print(6>>2)
print((6+3) - (9-4))
print((100-45) * 4)
print(100 + 5 * 3)

## Python Lists ##
fruits = ["banana","orange","mango","watermelon"]
print(fruits)
list1=["banana","apple","mango"]
list1[0]="pineapple"
list2=[5,2,4,3]
list3=[True,False,True]
print(list1)
print(list2)
print(list3)
list4=[5,True,"Bhargav",7,"abc"]
print(list4)

thislist = ["one","two","three"]
for x in thislist:
    print(x)

"""name = input("What is your name: ")
print('Hello ' + name)"""
#print(name)

"""list = ["honey","bhargav","sri"]
for i in range(len(list)):
    print(i)"""

"""print("Hello ,\"Bhargav\"")
name=input("Hello there what's your good name: ").strip().capitalize()
name = name.strip()
name= name.capitalize()
print(f"My name is {name}")"""

#thislist.clear()
#print(thislist)
colors=["red","orange","black","orange"]
xx=colors.count("orange")
print(xx)
colors.reverse()
print(colors)
colors.pop(2)
print(colors)
colors.sort()
print(colors)

######### Tuple ##########
thistuple = ("Men","Female","Others","old men","Female")
print(thistuple)
yy=list(thistuple)
yy[0]="Animals"
print(yy)
print(len(yy))
cars = ("BMW",)
print(cars)
print(type(cars))
  # Tuple() Constructor #
car = tuple(("Audi","Benz","Ferrari","Kia","Suzuki"))
print(car)
print(car[2])
print(car[-2])
print(car[1:4])
print(car[:4])
print(car[2:])
Vehicle = list(car)
Vehicle[4]="Rangerover"
car=tuple(Vehicle)
print(car)
b=("Suzuki",)
car +=b
print(car)
######
pens = ("Blue","Black","Red","Green")
y = ("Yellow",)
pens += y
print(pens)
## Remove an item in tuple ##
p=list(pens)
p.remove("Yellow")
pens = tuple(p)
print(pens)

##### Unpacking Tuple #####
fruit =("Grape","Karbuja","Goa",)
(Red,Green,Black) = fruit
print(Red)
print(Green)
print(Black)
####### Asterik * ###
fruit =("Grape","Goa","Karbuja","PineApple","Banana")
(Red,Green,*Black) = fruit
print(Red)
print(Green)
print(Black)

### Loop Tuples ###
names=("Bhargav","Honey","MuniChandra","Nagalakshmi")
for x in names:
    print(x)
######
for x in range(len(names)):
    print(names[x])

######
laptop=("dell","lenovo","aces","hp")
i=0
while i<len(laptop):
    print(laptop[i])
    i=i+1

## joint tuple ###
c =names + laptop
print(c)

## tuple methods ##
 # count()
numbers =(1,5,4,3,1,8,9,1)
x = numbers.count(1)
print(x)

#####  Sets #####
sets = {"Bhargav","Honey","Muni","Nag","Honey"}
print(sets)
print(len(sets))

set= {True,0,"Honey",1,False}
print(set)
print(len(set))
set1={"Bhargav","mango","Honey","Goa"}
set2={1,5,6,2,3,1}
set3={True,False,True}
print(set1)
print(set2)
print(set3)

### Add ###

set1.add("Muni")
print(set1)

#### Update ####
set2.update("4")
print(set2)
set1.update("muni")
print(set1)

## Remove / discard ##
set2.remove("4")
print(set2)
set2.discard(5)
print(set2)
set2.discard(5)
print(set2)
set1.pop()
print(set1)
set3.clear() # it returns the empty set
print(set3)

### Join Sets ###

Thisset ={"audi","ferrari","lamborgine","benz"}
Thisset1={"red","black","blue"}
#Thisset2=Thisset.union(Thisset1)
Thisset2=Thisset |Thisset1
print(Thisset2)
Thisset3 = Thisset2.union(names,fruit) # Multiple join sets
print(Thisset3)
##
Thisset3 = Thisset2 | sets | set # Multiple join sets
print(Thisset3)

## Jion Set and Tuple ##
Tuple=Thisset.union(laptop)
print(Tuple)

### Intersection ###
Tuple1= Tuple.intersection(Thisset)
print(Tuple1)
eat={"apple","banana","grape","lemon"}
Eat={"pemogranate","apple","orange","avacado"}
EAT=eat & Eat
print(EAT)


##### Dictionaries #####
thisdict={
    "name":"Bhargav",
    "age":"24",
    "city":"Hyderabad"
}
print(thisdict["name"])
print(thisdict)
###
dict={
    1:{
    "name":"Honey",
    "age":24,
    "city":"naidupet"
},
    2:{
    "name":"Muni",
    "age":33,
    "city":" SriKhalasti"
}
}
print(dict)
print(len(dict))

thisdict1={
    "name":"Nagalakshmi",
    "age":"30",
    "B.tech":False,
    "year":1992,
    "city":"Yandagandi"
}
print(thisdict1)