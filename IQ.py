# 1. Write a program to add two numbers without using (+) operator ?
num1= 5
num2=1
while num2 !=0:
    c=num1&num2
    num1=num1^num2
    num2=c<<1
print(num1)
