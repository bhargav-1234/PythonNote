import math
#Python Math:
'''
Python has a set of built-in math functions, including an extensive math module, 
that allows you to perform mathematical tasks on numbers.
'''

#Built-in Math Functions:
'''The min() and max() functions can be used to find the lowest or highest value in an iterable.'''

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#The abs() function returns the absolute (positive) value of the specified number:

x = abs(-7.25)

print(x)

#The pow(x, y) function returns the value of x to the power of y (xy).

x = pow(4, 3)

print(x)

#The Math Module:
'''
Python has also a built-in module called math, which extends the list of mathematical functions.

To use it, you must import the math module:
       'import math'
'''

'''
When you have imported the math module, you can start using methods and constants of the module.

The math.sqrt() method for example, returns the square root of a number:
'''

x = math.sqrt(6)
print(x)


'''
The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to 
its nearest integer, and returns the result:

'''

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1


#The math.pi constant, returns the value of PI (3.14...):

x = math.pi

print(x)

#Python math.acos() Method:
'''
The math.acos() method returns the arc cosine value of a number.

Note: The parameter passed in math.acos() must lie between -1 to 1.

Tip: math.acos(-1) will return the value of PI.

'''

print(math.acos(0.55))
print(math.acos(-0.55))
print(math.acos(0))
print(math.acos(1))
print(math.acos(-1))

#Python math.acosh() Method
'''
The math.acosh() method returns the inverse hyperbolic cosine of a number.

Note: The parameter passed in acosh() must be greater than or equal to 1.

'''
print (math.acosh(7))
print (math.acosh(56))
print (math.acosh(2.45))
print (math.acosh(1))

#Python math.asin() Method
'''The math.asin() method returns the arc sine of a number.

Note: The parameter passed in math.asin() must lie between -1 to 1.

Tip: math.asin(1) will return the value of PI/2, and math.asin(-1) will return the value of -PI/2.

'''

print(math.asin(0.55))
print(math.asin(-0.55))
print(math.asin(0))
print(math.asin(1))
print(math.asin(-1))

#Python math.asinh() Method
'''The math.asinh() method returns the inverse hyperbolic sine of a number.
'''
print(math.asinh(7))
print(math.asinh(56))
print(math.asinh(2.45))
print(math.asinh(1))

#Python math.atan() Method
'''The math.atan() method returns the arc tangent of a number (x) as a numeric value between -PI/2 and PI/2 radians.

Arc tangent is also defined as an inverse tangent function of x, where x is the value of the arc tangent is to be calculated.

'''
print (math.atan(0.39))
print (math.atan(67))
print (math.atan(-21))


#Python math.atan2() Method
'''The math.atan2() method returns the arc tangent of y/x, in radians. Where x and y are the coordinates of a point (x,y).

The returned value is between PI and -PI
'''

print(math.atan2(8, 5))
print(math.atan2(20, 10))
print(math.atan2(34, -7))

#Python math.atanh() Method
'''The math.atanh() method returns the inverse hyperbolic tangent of a number.

Note: The parameter passed in math.atanh() must lie between -0.99 to 0.99.

'''

print(math.atanh(0.59))
print(math.atanh(-0.12))

#Python math.comb() Method
'''The math.comb() method returns the number of ways picking k unordered outcomes from n possibilities, 
without repetition, also known as combinations.

Note: The parameters passed in this method must be positive integers.'''

# Initialize the number of items to choose from
n = 7

# Initialize the number of possibilities to choose
k = 5

# Print total number of possible combinations
print (math.comb(n, k))


#Python math.copysign() Method
'''The math.copysign() method returns a float consisting of the value of the first parameter and the sign(+/-) of the second parameter.'''

#Return the value of the first parameter and the sign of the second parameter
print(math.copysign(4, -1))
print(math.copysign(-8, 97.21))
print(math.copysign(-43, -76))

#Python math.cos() Method
'''The math.cos() method returns the cosine of a number.'''

# Return the cosine of different numbers
print (math.cos(0.00))
print (math.cos(-1.23))
print (math.cos(10))
print (math.cos(3.14159265359))

#Python math.cosh() Method
'''The math.cosh() method returns the hyperbolic cosine of a number (equivalent to (exp(number) + exp(-number)) / 2).

'''

# Return the hyperbolic cosine of different numbers
print (math.cosh(1))
print (math.cosh(8.90))
print (math.cosh(0))
print (math.cosh(1.52))


#Python math.degrees() Method
'''The mmath.degrees() method converts an angle from radians to degrees.

Tip: PI (3.14..) radians are equal to 180 degrees, which means that 1 radian is equal to 57.2957795 degrees.

Tip: See also math.radians() to convert a degree value into radians.'''

# Convert from radians to degrees:
print (math.degrees(8.90))
print (math.degrees(-20))
print (math.degrees(1))
print (math.degrees(90))

#Python math.dist() Method
'''The math.dist() method returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point.

Note: The two points (p and q) must be of the same dimensions.

'''

p = [3]
q = [1]

# Calculate Euclidean distance
print (math.dist(p, q))

p = [3, 3]
q = [6, 12]

# Calculate Euclidean distance
print (math.dist(p, q))


#Python math.erf() Method
'''The math.erf() method returns the error function of a number.

This method accepts a value between - inf and + inf, and returns a value between - 1 to + 1.'''


# Print error function for different numbers
print (math.erf(0.67))
print (math.erf(1.34))
print (math.erf(-6))

#Python math.erfc() Method
'''The math.erfc() method returns the complementary error function of a number.

This method accepts a value between - inf and + inf, and returns a value between 0 and 2.'''

# Print complementary error function for different numbers
print (math.erfc(0.67))
print (math.erfc(1.34))
print (math.erfc(-6))

#Python math.exp() Method
'''The math.exp() method returns E raised to the power of x (Ex).

'E' is the base of the natural system of logarithms (approximately 2.718282) and x is the number passed to it.'''

#find the exponential of the specified value
print(math.exp(65))
print(math.exp(-6.89))

#Python math.expm1() Method:
'''The math.expm1() method returns Ex - 1.

'E' is the base of the natural system of logarithms (approximately 2.718282) and x is the number passed to it.

This function is more accurate than calling math.exp() and subtracting 1.'''

#Return the exponential value of a number - 1
print(math.expm1(32))
print(math.expm1(-10.89))

#Python math.fabs() Method:
'''The math.fabs() method returns the absolute value of a number, as a float.

Absolute denotes a non-negative number. This removes the negative sign of the value if it has any.

Unlike Python abs(), this method always converts the value to a float value.

'''

#Print absolute values from numbers
print(math.fabs(-66.43))
print(math.fabs(-7))

#Python math.factorial() Method:
'''The math.factorial() method returns the factorial of a number.

Note: This method only accepts positive integers.

The factorial of a number is the sum of the multiplication, of all the whole numbers, from our specified number down to 1. 
For example, the factorial of 6 would be 6 x 5 x 4 x 3 x 2 x 1 = 720'''

#Return factorial of a number
print(math.factorial(9))
print(math.factorial(6))
print(math.factorial(12))

#Python math.floor() Method:
'''The math.floor() method rounds a number DOWN to the nearest integer, if necessary, and returns the result.

Tip: To round a number UP to the nearest integer, look at the math.ceil() method.

'''
# Round numbers down to the nearest integer
print(math.floor(0.6))
print(math.floor(1.4))
print(math.floor(5.3))
print(math.floor(-5.3))
print(math.floor(22.6))
print(math.floor(10.0))

#Python math.fmod() Method:
'''The math.fmod() method returns the remainder (modulo) of x/y.'''

# Return the remainder of x/y
print(math.fmod(20, 4))
print(math.fmod(20, 3))
print(math.fmod(15, 6))
print(math.fmod(-10, 3))
#print(math.fmod(0, 0))

#Python math.frexp() Method:
'''The math.frexp() method returns the mantissa and the exponent of a specified number, as a pair (m,e).

The mathematical formula for this method is: number = m * 2**e.

'''
#Return mantissa and exponent of numbers
print(math.frexp(4))
print(math.frexp(-4))
print(math.frexp(7))

#Python math.fsum() Method:
'''The math.fsum() method returns the sum of all items in any iterable (tuples, arrays, lists, etc.).

'''

# Print the sum of all items
print(math.fsum([1, 2, 3, 4, 5]))
print(math.fsum([100, 400, 340, 500]))
print(math.fsum([1.7, 0.3, 1.5, 4.5]))

#Python math.gamma() Method:
'''The math.gamma() method returns the gamma function at a number.

Tip: To find the log gamma value of a number, use the math.lgamma() method.'''

# Return the gamma function for different numbers
print(math.gamma(-0.1))
print(math.gamma(8))
print(math.gamma(1.2))
print(math.gamma(80))
print(math.gamma(-0.55))

#Python math.gcd() Method:
'''The math.gcd() method returns the greatest common divisor of the two integers int1 and int2.

GCD is the largest common divisor that divides the numbers without a remainder.

GCD is also known as the highest common factor (HCF).

Tip: gcd(0,0) returns 0.'''

#find the  the greatest common divisor of the two integers
print (math.gcd(3, 6))
print (math.gcd(6, 12))
print (math.gcd(12, 36))
print (math.gcd(-12, -36))
print (math.gcd(5, 12))
print (math.gcd(10, 0))
print (math.gcd(0, 34))
print (math.gcd(0, 0))

#Python math.hypot() Method:
'''The math.hypot() method returns the Euclidean norm. The Euclidian norm is the distance from the origin to the coordinates given.

Prior Python 3.8, this method was used only to find the hypotenuse of a right-angled triangle: sqrt(x*x + y*y).

From Python 3.8, this method is used to calculate the Euclidean norm as well. For n-dimensional cases, 
the coordinates passed are assumed to be like (x1, x2, x3, ..., xn). 
So Euclidean length from the origin is calculated by sqrt(x1*x1 + x2*x2 +x3*x3 .... xn*xn).
'''

#set perpendicular and base
parendicular = 10
base = 5

#print the hypotenuse of a right-angled triangle
print(math.hypot(parendicular, base))

#Python math.isclose() Method:
'''The math.isclose() method checks whether two values are close to each other, or not. Returns True if the values are close, otherwise False.

This method uses a relative or absolute tolerance, to see if the values are close.

Tip: It uses the following formula to compare the values: abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

'''

#compare the closeness of two values
print(math.isclose(1.233, 1.4566))
print(math.isclose(1.233, 1.233))
print(math.isclose(1.233, 1.24))
print(math.isclose(1.233, 1.233000001))

#Python math.isfinite() Method:
'''The math.isfinite() method checks whether a number is finite or not.

This method returns True if the specified number is a finite number, otherwise it returns False.'''

# Check whether the values are finite or not
print(math.isfinite(2000))
print(math.isfinite(-45.34))
print(math.isfinite(+45.34))
print(math.isfinite(math.inf))
print(math.isfinite(float("nan")))
print(math.isfinite(float("inf")))
print(math.isfinite(float("-inf")))
print(math.isfinite(-math.inf))
print(math.isfinite(0.0))

#Python math.isinf() Method:
'''The math.isinf() method checks whether a number is infinite or not.

This method returns True if the specified number is a positive or negative infinity, otherwise it returns False.

'''
# Check whether the values are infinite or not
print(math.isinf(56))
print(math.isinf(-45.34))
print(math.isinf(+45.34))
print(math.isinf(math.inf))
print(math.isinf(float("nan")))
print(math.isinf(float("inf")))
print(math.isinf(float("-inf")))
print(math.isinf(-math.inf))

#Python math.isnan() Method:
'''The math.isnan() method checks whether a value is NaN (Not a Number), or not.

This method returns True if the specified value is a NaN, otherwise it returns False.'''

# Check whether some values are NaN or not
print (math.isnan (56))
print (math.isnan (-45.34))
print (math.isnan (+45.34))
print (math.isnan (math.inf))
print (math.isnan (float("nan")))
print (math.isnan (float("inf")))
print (math.isnan (float("-inf")))
print (math.isnan (math.nan))

#Python math.isqrt() Method:
'''The math.isqrt() method rounds a square root number downwards to the nearest integer.

Note: The number must be greater than or equal to 0.'''

# Print the square root of different numbers
print (math.sqrt(10))
print (math.sqrt (12))
print (math.sqrt (68))
print (math.sqrt (100))

# Round square root downward to the nearest integer
print (math.isqrt(10))
print (math.isqrt (12))
print (math.isqrt (68))
print (math.isqrt (100))

#Python math.ldexp() Method:
'''The math.ldexp() method returns  x * (2**i) of the given numbers x and i, which is the inverse of math.frexp().
'''

#Python math.lgamma() Method:
'''The math.lgamma() method returns the natural logarithm gamma value of a number.

Tip: We can find also find the log gamma value by using the math.gamma() method to find the gamma value, 
and then use the math.log() method to calculate the log of that value.

Tip: The gamma value is equal to factorial(x-1).

'''

# Return the log gamma value of different numbers
print (math.lgamma(7))
print (math.lgamma(-4.2))


#Python math.log() Method:
'''The math.log() method returns the natural logarithm of a number, or the logarithm of number to base.
'''

# Return the natural logarithm of different numbers
print(math.log(2.7183))
print(math.log(2))
print(math.log(1))

#Python math.log10() Method:
'''The math.log10() method returns the base-10 logarithm of a number.
'''
# Return the base-10 logarithm of different numbers
print(math.log10(2.7183))
print(math.log10(2))
print(math.log10(1))

#Python math.log1p() Method:
'''The math.log1p() method returns log(1+number), computed in a way that is accurate even when the value of number is close to zero.

'''

# Return the log(1+number) for different numbers
print(math.log1p(2.7183))
print(math.log1p(2))
print(math.log1p(1))


#Python math.log2() Method:
'''The math.log2() method returns the base-2 logarithm of a number.
'''
# Return the base-2 logarithm of different numbers
print(math.log2(2.7183))
print(math.log2(2))
print(math.log2(1))

#Python math.perm() Method:
'''The math.perm() method returns the number of ways to choose k items from n items with order and without repetition.

Note: The k parameter is optional. If we do not provide one, this method will return n! (for example, math.perm(7) will return 5040).

'''

# Initialize the number of items to choose from
n = 7

# Initialize the number of items to choose
k = 5

# Print the number of ways to choose k items from n items
print (math.perm(n, k))

#Python math.pow() Method:
'''The math.pow() method returns the value of x raised to power y.

If x is negative and y is not an integer, it returns a ValueError.

This method converts both arguments into a float.

Tip: If we use math.pow(1.0,x) or math.pow(x,0.0), it will always returns 1.0.'''

#Return the value of 9 raised to the power of 3
print(math.pow(9, 3))

#Python math.prod() Method:
'''The math.prod() method returns the product of the elements from the given iterable.
'''

sequence = (2, 2, 2)

#Return the product of the elements
print(math.prod(sequence))

#Python math.radians() Method:
'''The math.radians() method converts a degree value into radians.

Tip: See also math.degrees() to convert an angle from radians to degrees.

'''

# Convert different degrees into radians
print(math.radians(180))
print(math.radians(100.03))
print(math.radians(-20))

#Python math.remainder() Method;
'''The math.remainder() method returns the remainder of x with respect to y.
'''

# Return the remainder of x/y
print (math.remainder(9, 2))
print (math.remainder(9, 3))
print (math.remainder(18, 4))


#Python math.sin() Method:
'''The math.sin() method returns the sine of a number.

Note: To find the sine of degrees, it must first be converted into radians with the math.radians() method (see example below).

'''

# Return the sine of different values
print (math.sin(0.00))
print (math.sin(-1.23))
print (math.sin(10))
print (math.sin(math.pi))
print (math.sin(math.pi/2))

#Python math.sinh() Method:
'''The math.sinh() method returns the hyperbolic sine of a number.
'''

# Return the hyperbolic sine of different values
print(math.sinh(0.00))
print(math.sinh(-23.45))
print(math.sinh(23))
print(math.sinh(1.00))
print(math.sinh(math.pi))

#Python math.tan() Method:
'''The math.tan() method returns the tangent of a number.
'''

# Return the tangent of different numbers
print (math.tan(90))
print (math.tan(-90))
print (math.tan(45))
print (math.tan(60))

#Python math.tanh() Method:
'''The math.tanh() method returns the hyperbolic tangent of a number.
'''

# Return the hyperbolic tangent of different numbers
print(math.tanh(8))
print(math.tanh(1))
print(math.tanh(-6.2))

#Python math.trunc() Method:
'''The math.trunc() method returns the truncated integer part of a number.

Note: This method will NOT round the number up/down to the nearest integer, but simply remove the decimals.'''

# Return the truncated integer parts of different numbers
print(math.trunc(2.77))
print(math.trunc(8.32))
print(math.trunc(-99.29))


#Math Constants:

#Python math.e Constant:
'''The math.e constant returns the Eular's number: 2.718281828459045.
'''
# Print the value of E
print (math.e)

#Python math.inf Constant:
'''The math.inf constant returns a floating-point positive infinity.

For negative infinity, use -math.inf.

The inf constant is equivalent to float('inf').'''

# Print the positive infinity
print (math.inf)

# Print the negative infinity
print (-math.inf)

#Python math.nan Constant:
'''The math.nan constant returns a floating-point nan (Not a Number) value. This value is not a legal number.

The nan constant is equivalent to float('nan').'''

# Print the value of nan
print (math.nan)

#Python math.pi Constant:
'''The math.pi constant returns the value of PI: 3.141592653589793.

Note: Mathematically PI is represented by π.'''


#Python math.tau Constant:
'''The math.tau constant returns the value of tau, which is 6.283185307179586.

It is defined as the ratio of the circumference to the radius of a circle. Tau is a circle constant and the value is equivalent to 2π.

Note: Mathematically tau is represented by τ.

'''

# Print the value of tau
print (math.tau)

