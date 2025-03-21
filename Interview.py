import pdb
# Converting an integer into decimal
import decimal
integer = 10
print(decimal.Decimal(integer))
string ="1234"
print(decimal.Decimal(string))

# Reversing a string using an extended slicing technique
String ="Python programming"
print(String[::-1])

#counting vowels in a given word
vowel=['a','e','i','o','u']
word="programming"
count=0
for character in word:
    if character in vowel:
        count += 1
    
print(count)

# counting consonants in a given word
Vowel=["a","e","i","o","u"]
Word= "programming"
Count =0
for character in Word:
    if character not in Vowel:
        Count +=1
print(Count)

# writing the FIBONACCI series
fib = [0,1]
   #range starts from 0 by default
n=5
for i in range(n):
    fib.append(fib[-1]+fib[-2])

  #converting the list of integers to strings
print(', '.join(str(e) for e in fib))

# finding the maximum number in a list
numberList =[12,56,25,3,8,78,33,1]
max=numberList[0]
for num in numberList:
    if max <num:
        max =num
print(max)

# finding the minimum  number in a list
numberList =[12,56,25,3,8,78,33,1]
min =numberList[0]
for num in numberList:
    if min >num:
        min = num
print(min)

# finding thr middle element in the list
numberList =[12,56,25,3,8,78,33,1]
midElement =int(len(numberList)/2)
print(numberList[midElement])

#Converting a list into string
list=["p","y","t","h","o","n"]
string="".join(list)
print(string)

#Adding two list elements together
list1=[1,2,3]
list2=[4,5,6]
res_lst=[]
for i in range(0, len(list1)):
    res_lst.append(list1[i] + list2[i])
print(res_lst)

# Comparing two strings for ANAGRAMS
str1="Listen"
str2="Silent"
 
str1=str1.replace(" "," ").upper()
str2=str2.replace(" "," ").upper()

if sorted(str1) == sorted(str2):
    print("True")

else:
    print("False")

# Checking for PALINDROME ussing extended slicing technique
str ="BHARGAV".lower()

if str == str[::-1]:
    print("True")
else:
    print("False")

# counting the whitespace in a string
str ="p p  program "
print(str.count(" "))

#counting digits, letters and whitespace in a string

import re # import regular expression library
name = "Python is  1"
digitCount=re.sub("[^0-9]","",name)
letterCount=re.sub("[^a-zA-Z]","",name)
spaceCount =re.findall("[ \s]", name)
print(len(digitCount))
print(len(letterCount))
print(len(spaceCount))

# counting special characters in string
def count_spl_char(string):
    spl_char="!@#$%^&*()<>?/\[]{};:~'"
    count=0
    for i in string:
        if i in spl_char:
            count+=1
    return count
text ='Hello! How are you ? #specialchars ! 123'
result =count_spl_char(text)
print(count)

# removing all whitespace in a string
#1.
white = 'j a n u'
spaces= re.compile(r'\s+')
result=re.sub(spaces,"",white)
print(result)

#2.
white = 'j a n u'
spaces="".join(char for char in white if char !=" ")
print(spaces)

#3.
white = 'j a n u'
spaces=white.replace(" ","")
print(spaces)  

#Building a pyramid in python

# def pyramid(n):
#         for i in range(n):
#             for j in range(i,n):
#                 print(" ",end="")
#             #pdb.set_trace()
#             for j in range(i+1):
#                 print('*',end="")
#             for j in range(i):
#                 print('*',end="")
#             print(' ')
# pyramid(6)

#2.
# num = int(input('enter odd number:'))
# cnt=num//2
# scnt=1
# for i in range(cnt+1):
#     print(cnt*" "+"*"*scnt)
#     cnt=cnt-1
#     scnt=scnt+2
# scnt=num-2
# cnt=1
# for i in range(num//2):
#         print(cnt*" "+"*"*scnt)
#         scnt=scnt-2
#         cnt=cnt+1

#Randomizing the items of a list in python
from random import shuffle

lst=['python','is','easy']
shuffle(lst)
print(lst)

#creating a generator to produce first n prime numbers
# def isprime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#         return True

# def prime_generator(n):
#     num=2
#     while n:
#         if isprime(num):
#             '''FRND is an online friendship app designed to facilitate connections between users seeking to meet new friends. 
#             This app is particularly aimed at individuals aged 12 and above and allows users to engage in audio and video calls, 
#             enhancing the experience of forming friendships in a virtual space. Available for the Android platform, 
#             users can easily download FRND and start exploring a community dedicated to friendship.'''
#         yield num
#         n-=1
#         num+=1
# x =int(input('enter no. of prime numbers required '))
# it = prime_generator(x)
# for e in it:
#     print(e,end='') 

# program to check if a given number is prime or not
# def prime_no(n):
#     Flag = False
#     if n < 2:
#         return Flag
#     else:
#         for i in range(2,n):
#             if n%i == 0:
#                 return Flag
#             else:
#                 Flag = True
#                 return Flag     
# num=int(input('Enter a number: '))
# print(prime_no(num))

#2.
# def prime_no(n):
#     Flag = False
#     if n < 2:
#         return Flag
#     else:
#         for i in range(2,n):
#             if n%i == 0:
#                 return Flag
#         Flag = True
#         return Flag     
# numm=int(input('Enter a number: '))
# print(prime_no(numm))
    
# implementing variable length arguments in python
def average(*t):
    avg=sum(t)/len(t)
    return avg
result1 = average(35,5,65,22,87,34,2,57)
result2= average(5,10,15,20,25,30,35,40,45,50)
print("Average is :",result1)
print("Average is :",result2)

#creating the instance number variables in python
class Test:
    def __init__(self):
          # first instance variable inside in init function
          self.a =5
    def f1(self):
        # second instance variable inside function f1
        self.b=10
    
t1=Test()
t2=Test()
t1.f1()
# 3rd instance variable
t1.c=15
print(t1.__dict__)
print(t2.__dict__)

# addition using lambda function
f =lambda a,b :a+b
r=f(3,7)
print(r)
  # OR
print((lambda a,b :a+b)(3,7))

#finding factorial using the lambda function
# f=lambda n: 1 if n==0 else n*f(n-1)
# print(f(5))

# num= int(input("Enter a number: "))
#   #7
# factorial=1
# if num < 0:
#     print("Sorry, factorial does not exist for negative numbers")
# elif num==0:
#      print("The factorial of 0 is 1")
# else:
#     for i in range(1, num+1):
#         factorial=factorial*i
#     print(f"the factorial of {num} is",factorial)
    #5040

# list compression (to create a list in single line)
   
    # list of even numbers
l1=[2*e for e in range(1, 10)]
print(l1)

# OR
 # to create a list of even numbers from a given list 
list=[23,56,65,22,62,32,65,76,33,99]
l2=[e for e in list if e%2==0]
print(l2)

# what is the use of spilt and join function of str ?
  #split- to convert string into list of string
s="What is right in your mind is right in your world"
s1=s.split(" ")
print(s1)
s1=s1[::-1]
print(s1)
  #join- to convert the list again into string
print(" ".join(s1))

# global and local variable

x=5 # global variable
def f1():
    global x
    x=12 # global varaible updated
    y=10 #local variable
    print("x=%d y=%d"%(x,y))

f1()
print(x)

# type of conversion basics
x =int('123')
y=float('123.456')
a=complex(1+3j)
# b=str(12)
c=bool('True')
d=bin(25) #binary
e=oct(25)
f=hex(25)
g=ord('A') #char to unicode
h=chr(98) #unicode to character
print(x,y,a,c,d,e,f,g,h,sep="\n")

# type conversion

x=6
print(type(x))
s='123'
print(type(s))
# print(str(x)+s)
print(x+int(s)) 

# what is python decorator
   # function decorator
def welcome(fx):
    def mfx(*t,**d):
        print("before hello function")
        fx(*t,**d)