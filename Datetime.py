#python Datetime:
import datetime
#Python Dates:
'''A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

'''
x = datetime.datetime.now()

print(x)

#Date Output:
'''
When we execute the code from the example above the result will be:

2023-04-27 15:36:58.078792
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.

Here are a few examples, you will learn more about them later in this chapter.
'''

x = datetime.datetime.now()

print(x.year)
print(x.month)
print(x.strftime("%A"))


#Create Date Objects:
'''
To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.
'''

x = datetime.datetime(2023, 4, 27) 

print(x)

'''The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), 
but they are optional, and has a default value of 0, (None for timezone).

'''

#The strftime():
'''
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string.
'''

x = datetime.datetime.now() 

print(x.strftime("%B"))
print(x.strftime("%w"))
print(x.strftime("%m"))
print(x.strftime("%d"))
print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%H"))
print(x.strftime("%S"))
print(x.strftime("%I"))
print(x.strftime("%p"))
print(x.strftime("%f"))
print(x.strftime("%M"))
print(x.strftime("%Z"))
print(x.strftime("%z"))
print(x.strftime("%j"))
print(x.strftime("%U"))
print(x.strftime("%W"))
print(x.strftime("%x"))
print(x.strftime("%X"))
print(x.strftime("%G"))
print(x.strftime("%V"))
print(x.strftime("%c"))

