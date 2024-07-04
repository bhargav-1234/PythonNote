# Python  File Handling:

#Python file open():
'''File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.
'''

#File handling:
'''The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode.
   
       "t" - Text - Default value. Text mode

        "b" - Binary - Binary mode (e.g. images)
'''

  #Syntax:
'''To open a file for reading it is enough to specify the name of the file:
'''
     #f = open("demofile.txt")

     #f = open("demofile.txt", "rt")

'''Because "r" for read, and "t" for text are the default values, you do not need to specify them.
'''
      #Note: Make sure the file exists, or else you will get an error.


#Open a File on the Server:
'''Assume we have the following file, located in the same folder as Python.
'''
    #demofile.txt:
'''To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file.
'''
f = open("demofile.txt", "r")

print(f.read())

