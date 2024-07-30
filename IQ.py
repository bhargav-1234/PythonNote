# 1. Write a program to add two numbers without using (+) operator ?
num1= 5
num2=1
while num2 !=0:
    c=num1&num2
    num1=num1^num2
    num2=c<<1
print(num1)

# ---------------------- #
a =[1,2,3,4,5]
for i in a:
    a.remove(i)
print(a)

# ---------------------- #
# what will be the output of the code ?
a =[1,2,3,4]
b = a
a.append(5)
print(b)  # output: [1, 2, 3, 4, 5]

# ---------------------- #
# what is the output of C

A ={2,3,4,5,6,7}
B={2,5,8,9}
C = A^B
print(C) # output: {3, 4, 6, 7, 8, 9}

# Q: remove the duplicates from the list:

numbers=[1,2,2,3,4,4,5]
unique_numbers =list(set(numbers))
print("unique_numbers :", unique_numbers)  # output : unique_numbers : [1, 2, 3, 4, 5]

# Q: what will be the output of following code ?
a = [1,2,3,4,1,2,3,4]
print(a.index(2,3))  # output : 5

# ------------------------ #

my_list =[1,2,3,4,5]
my_list.pop(2)
print(my_list) # output : [1,2,4,5]

# ------------------------ #
# l =[1,2,3,4,5,7]
# l.insert(6)
# print(l)  # output: error

# ------------------------- #
a ="Python"
b= len(a)
c =0
for i in range(1,b+1):
    c =c*i
print(c) # output :0

## ----- S pattern ----- ###
for i in range(7):
    for j in range(7):
        if i == 0 or i == 3 or i == 6:
            print("*", end="")
        elif(i < 3 and j == 0):
            print("*", end="")
        elif(i > 3 and j == 6):
            print("*", end="")
        else:
            print(end=" ") # output is "s" pattern
    print()

#-------------------------#
# Q: what will be the output ?
a=0
for i in range(8):
    pass
    a=a+1
print(a)   # output: 8

# ---------------Bubble sort Algorithm------------- #

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
print(bubble_sort([64,34,12,22,11,90])) # output : [11, 12, 22, 34, 64, 90]

# Q: caluculate the area of a circle ?

import math
def  area_of_circle(radius):
    return math.pi * (radius ** 2)
print(area_of_circle(5))  # output: 78.53981633974483

# -------------------------- #
word ="Python"
x = ""
for i in word:
    x += i
    print(x) 
# output:
# Py
# Pyt
# Pyth
# Pytho
# Python

# -------------------------- #
# Q : find the most frequent element in the list [1,2,2,3,3,3,4] ?
from collections import Counter

def most_frequent(lst):
    count = Counter(lst)
    return count.most_common(1)[0][0]
print(most_frequent([1,2,2,3,3,3,4]))  #output : 3
#-------------------------#
a = 5
b = (a == 2)
print(b+3)  # 3
# ------------------ #
lst = [10,15,5,12]
lst1=0
for i in lst:
    if i>lst1:
        lst1=i
print(lst1)  # 5

# ------------------------- #
 # comparsion operator is also called rational operator

# --------------------------- #
a = 1
for i in range(2,6):
    for j in range(2,6):
        if i%j == 0:
            a=a+1
print(a)   # output:6

# -------------------------- #

# Q: what will be the output of the following code ?
x ="5"
y=2
result=int(x) * y
print(result)  # 10
# -------------------------- #
sets={1,2,3}
sets.update([4,5,6])
print(sets) # {1, 2, 3, 4, 5, 6}

# --------------------------- #
a,b,c =5,6,0
c -= (-a+b)*(-a-b)
print(c)    # 11    
# --------------------------- #
a ={1,1,1,1,2,2,6,6,6,6}
b =list(a)
print(b[2]) # 6 (sets doesn't allows the duplicate values)
# --------------------------- #
x=y=[3]
x =x+y
print(x,y) # [3, 3] [3]

# --------------------------- #
#1.Using ASCII values to print "Hello World"
hello = chr(72) + chr(101) + chr(108) + chr(108) + chr(111)
world = chr(87) + chr(111) + chr(114) + chr(108) + chr(100)
print(hello + " " + world)

#2.
# Use join with map to construct and print the string
print(' '.join(map(chr, [72, 101, 108, 108, 111])) + ' ' + ' '.join(map(chr, [87, 111, 114, 108, 100])))

#3.
# Use format strings with ASCII values
hello = ''.join(chr(c) for c in [72, 101, 108, 108, 111])
world = ''.join(chr(c) for c in [87, 111, 114, 108, 100])

print(f"{hello} {world}")

# ------------- #
a=[1,6,8]
b=[2,3]
c=a.append(b)
print(a)  #[1,6,8,[2,3]]
print(a[-1]) # [2,3]

# ------------------------- #
def fun(x):
    return x+1
print(fun(2)*fun(3))  # 12

# ------------------------- #
a=[11,12,13,14,15]
b= int(len(a)//2)
print(a[b]) # 13

# ------------------------ #
a=[1,2,3,4,5,6]
for a[-1] in a:
    print(a[-1]) 
print(8/4+2) # 4.0

# Q. what will be the output of the followwing code ?
x={1,2,3}
y={3,4,5}
print(x & y)  # {3}









