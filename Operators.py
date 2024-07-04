##########################"Python Operators"############################
#Python Operator:
'''
Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values.
'''

print(10 + 5)

"""
Python divides the operators in the following groups:

*.Arithmetic operators
*.Assignment operators
*.Comparison operators
*.Logical operators
*.Identity operators
*.Membership operators
*.Bitwise operators

"""

#Arithmetic operators:
'''Arithmetic operators are used with numeric values to perform common mathematical operations.'''

#addtion('+'):
x = 2
y = 10

print(x + y)

#Subtraction('-'):
x = 5
y = 3

print(x - y)

#Multiplication('*'):
x = 2
y = 4

print(x * y)

#Division('/'):
x = 15
y = 4

print(x / y)

#Modulus('%'):
x = 5
y = 2

print(x  % y)

#Exponential('**')
x = 5
y = 4

print(x ** y)

#Floor division('//'):

x = 5
y = 2

print(x // y)

#Assignment Operator:
'''Assignment operators are used to assign values to variables.'''

# '=':
x = 10
print(x)

# '+=':
x += 10
print(x)

# "-=":
x -= 20
print(x)

#'*=':
x = 4
x *= 2
print(x)

#'/=':
x = 5
x /= 3
print(x)

#'%=':
x = 4
x %= 8
print(x)

#'//=':
x = 6
x //= 4
print(x)

#'**=':
x = 2
x **= 4
print(x)

#'&=':
x = 5
x &= 5
print(x)

#'|=':
x = 8
x |= 4
print(x)

#'^=':
x = 4
x ^= 2
print(x)

#'>>=':
x = 5

x >>= 3

print(x)

#'<<=':
x = 5
x <<= 3
print(x)

#Comparision Operators;
'''Comparison operators are used to compare two values.'''

#Equal("=="):
x = 5
y = 2
print(x == y)

#Not Equal(!=):
x = 5
y = 2
print(x != y)

#Greater than(>):
x = 6
y = 2
print(x > y)

#Less than(<):
x = 5
y = 12
print(x < y)

#Greater than or Equal to(>=):
x = 10
y = 5
print(x >= y)
####
x = 5
y = 5
print(x >= y)

#Less than or Equal to(<=):
x = 1
y = 2
print(x <= y)

#Logical Operators:
'''Logical operators are used to combine conditional statements.'''

#and:
'''Returns True if both statements are true	'''
x = 5
print(x < 2 and x > 6)

#or:
'''Returns True if one of the statements is true'''
x = 5
print(x < 2 or x > 4)

#not:
'''Reverse the result, returns False if the result is true'''
x = 5
print(not(x <2 and x >4))

#Identity Operators:
'''Identity operators are used to compare the objects, not if they are equal, 
but if they are actually the same object, with the same memory location
'''

#is:
'''Returns True if both variables are the same object'''
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


#is not:
'''Returns True if both variables are not the same object'''
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

#Memberships Operator:
'''Membership operators are used to test if a sequence is presented in an object'''

#in:
'''Returns True if a sequence with the specified value is present in the object'''

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

#not in:
'''Returns True if a sequence with the specified value is not present in the object'''

x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list


#Bitwise Operators:
'''Bitwise operators are used to compare (binary) numbers'''

#'AND(&)':
print(6 & 3)



"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

#'OR(|)':
print(6 | 3)


"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

#XOR(^):
'''Sets each bit to 1 if only one of two bits is 1'''

print(6 ^ 3)


"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

#NOR(~):
'''Inverts all the bits'''

print(~3)



"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""

#Zero fill left shift(<<):
print(3 << 2)


"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""


#Signed right shift(>>):
print(8 >> 2)



"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

#Operator Precedence:
'''Operator precedence describes the order in which operations are performed.'''

print((6 + 3) - (6 + 3))

"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""

print(100 + 5 * 3)

"""
Multiplication has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + 15 = 115
"""

