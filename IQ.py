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



