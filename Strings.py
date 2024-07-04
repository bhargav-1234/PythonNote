######################"Python Strings"#######################

#Strings:
"""Strings in python are surrounded by either single quotation marks, or double quotation marks.

   'hello' is the same as "hello".

    You can display a string literal with the print() function"""

print("Hello")
print('Hello')

a = "Bhargav"  # assign String to a variable
print(a)

# Multiline String:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Strings are Arrays:
"""Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string."""

a = "hello, world"
print(a[2])

# Looping Through the String:
"""Since strings are arrays, we can loop through the characters in a string, with a for loop."""

for x  in "banana":
    print(x)

# String Length:
"""To get the length of a string, use the len() function."""

print(len(a))

# Check String:
"""To check if a certain phrase or character is present in a string, we can use the keyword 'in'."""

txt = "Bhargav is the best man in the world and also honest man"
print("best" in txt)

  # Use it in an 'if statement':
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Check if NOT:
"""To check if a certain phrase or character is NOT present in a string, we can use the keyword 'not in'."""
a = "Never give up , untill reach your success"
print("good" not in a)
   
  # Use it in an 'if statement':
if "good" not in a:
   print('yes')

# Slicing Strings:
  #Slicing:
"""1.You can return a range of characters by using the slice syntax.
   2.Specify the start index and the end index, separated by a colon, to return a part of the string."""

a = "hello, world"
print(a[2:5])

  # slice from the start
print(a[:5])

  # slice from the end
print(a[3:])

  #Negetive Indexing
"""Use negative indexes to start the slice from the end of the string:"""
print(a[-5:-2])

#Modify String:
'''Python has a set of built-in methods that you can use on strings.'''
 #Upper case
a = "bhargav"
print(a.upper())
 #Lower case
a = "HARIKA"
print(a.lower())

# Remove Whitespace:
'''Whitespace is the space before and/or after the actual text, and very often you want to remove this space.'''

  #(The strip() method removes any whitespace from the beginning or the end)
a = "hello Bhargav"
print(a.strip())

# Replacing String:
'''The "replace()" method replaces a string with another string:'''

a = "Bhargav, How are you ?"
print(a.replace("Bhargav,", "Harika"))

# Split String:
'''The split() method returns a list where the text between the specified separator becomes the list items.'''
    #The "split()" method splits the string into substrings if it finds instances of the separator:
a = "hello, world"
print(a.split(","))

# Python String Methods:
  #  Method	                             Description
""" capitalize()     	     Converts the first character to upper case
    casefold()	             Converts string into lower case
    center()	             Returns a centered string
    count()	                 Returns the number of times a specified value occurs in a string
    encode()	             Returns an encoded version of the string
    endswith()	             Returns true if the string ends with the specified value
    expandtabs()	         Sets the tab size of the string
    find()	                 Searches the string for a specified value and returns the position of where it was found
    format()	             Formats specified values in a string
    format_map()	         Formats specified values in a string
    index()	                 Searches the string for a specified value and returns the position of where it was found
    isalnum()	             Returns True if all characters in the string are alphanumeric
    isalpha()	             Returns True if all characters in the string are in the alphabet
    isascii()	             Returns True if all characters in the string are ascii characters
    isdecimal()	             Returns True if all characters in the string are decimals
    isdigit()	             Returns True if all characters in the string are digits
    isidentifier()	         Returns True if the string is an identifier
    islower()	             Returns True if all characters in the string are lower case
    isnumeric()	             Returns True if all characters in the string are numeric
    isprintable()	         Returns True if all characters in the string are printable
    isspace()	             Returns True if all characters in the string are whitespaces
    istitle()	             Returns True if the string follows the rules of a title
    isupper()	             Returns True if all characters in the string are upper case
    join()	                 Converts the elements of an iterable into a string
    ljust()	                 Returns a left justified version of the string
    lower()	                 Converts a string into lower case
    lstrip()	             Returns a left trim version of the string
    maketrans()	             Returns a translation table to be used in translations
    partition()	             Returns a tuple where the string is parted into three parts
    replace()	             Returns a string where a specified value is replaced with a specified value
    rfind()	                 Searches the string for a specified value and returns the last position of where it was found
    rindex()	             Searches the string for a specified value and returns the last position of where it was found
    rjust()	                 Returns a right justified version of the string
    rpartition()	         Returns a tuple where the string is parted into three parts
    rsplit()	             Splits the string at the specified separator, and returns a list
    rstrip()	             Returns a right trim version of the string
    split()	                 Splits the string at the specified separator, and returns a list
    splitlines()	         Splits the string at line breaks and returns a list
    startswith()	         Returns true if the string starts with the specified value
    strip()	                 Returns a trimmed version of the string
    swapcase()	             Swaps cases, lower case becomes upper case and vice versa
    title()	                 Converts the first character of each word to upper case
    translate()	             Returns a translated string
    upper()	                 Converts a string into upper case
    zfill()	                 Fills the string with a specified number of 0 values at the beginning"""

  #capitalize():
'''The "capitalize()" method returns a string where the first character is upper case, and the rest is lower case.'''

txt = "hello, and welcome to my world."

x = txt.capitalize()   #Syntax: string.capatalize()

print (x)

  #casefold():
'''The casefold() method returns a string where all the characters are lower case.

This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, 
meaning that it will convert more characters into lower case, and will find more matches 
when comparing two strings and both are converted using the casefold() method. '''

txt = "Hello, Bhargav how are you ?"
x = txt.casefold()  #Syntax:string.casefold()
print(x)

   #center():
'''The center() method will center align the string, using a specified character (space is default) as the fill character.'''

txt = "Bhargav"
x = txt.center(20)  #Syntax:string.center(length, character)
print(x)

   #count():
'''The count() method returns the number of times a specified value appears in the string.'''

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")  #Syntax:string.count(value, start, end)

print(x)

   #encode():
'''The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.'''

txt = "My name is Ståle"

x = txt.encode()    #string.encode(encoding=encoding, errors=errors)

print(x)
#####
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

   #endswith():
'''The endswith() method returns True if the string ends with the specified value, otherwise False.'''

txt = "Hello, welcome to my world."

x = txt.endswith(".")   #Syntax:string.endswith(value, start, end)

print(x)
#####
txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)

print(x)

   #expandtabs():
'''The expandtabs() method sets the tab size to the specified number of whitespaces.'''

txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2) #Syntax:string.expandtabs(tabsize)

print(x)

   #find():
'''
The find() method finds the first occurrence of the specified value.

The find() method returns -1 if the value is not found.

The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)

'''

txt = "Hello, welcome to my world."

x = txt.find("welcome")  #Syntax:string.find(value, start, end)

print(x)

   #format():
'''
The format() method formats the specified value(s) and insert them inside the string's placeholder.

The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

The format() method returns the formatted string.

'''

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))  #Syntax:string.format(value1, value2...)
#####
   #Placeholders:
'''The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.'''

#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)

   #index():
'''
The index() method finds the first occurrence of the specified value.

The index() method raises an exception if the value is not found.

The index() method is almost the same as the find() method, 
the only difference is that the find() method returns -1 if the value is not found. (See example below)

'''

txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

   #isalnum()
'''The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
Example of characters that are not alphanumeric: (space)!#%&? etc.
'''

txt = "Company 12"

x = txt.isalnum()

print(x)
####
txt = "Company12"

x = txt.isalnum()  #Syntax:string.isalnum()

print(x)

  #isalpha():
'''The isalpha() method returns True if all the characters are alphabet letters (a-z).'''

txt = "CompanyX"

x = txt.isalpha()  #Syntax:string.isalpha()

print(x)
####
txt = "Company10"

x = txt.isalpha()  #Syntax:string.isalpha()

print(x)

   #isascii();
'''The isascii() method returns True if all the characters are ascii characters  (a-z).'''
       #Syntax:string.isascii()
   
   #isdecimal():
'''The isdecimal() method returns True if all the characters are decimals (0-9).

   This method is used on unicode objects.
'''

txt = "\u0033" #unicode for 3

x = txt.isdecimal()   #Syntax:string.isdecimal()

print(x)

   #isdigit():
'''
The isdigit() method returns True if all the characters are digits, otherwise False.

Exponents, like ², are also considered to be a digit.

'''
   
txt = "50800"

x = txt.isdigit()  #Syntax:string.isdigit()

print(x)
#####
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())

   #isidentifier():
'''
The isidentifier() method returns True if the string is a valid identifier, otherwise False.

A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). 
A valid identifier cannot start with a number, or contain any spaces.
'''

txt = "Demo"

x = txt.isidentifier()  #Syntax:string.isidentifier()

print(x)


   #islower():
'''
The islower() method returns True if all the characters are in lower case, otherwise False.

Numbers, symbols and spaces are not checked, only alphabet characters.

'''

txt = "hello world!"

x = txt.islower()  #Syntax:string.islower()

print(x)

   #isnumeric():
'''
The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.

Exponents, like ² and ¾ are also considered to be numeric values.

"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.

'''

txt = "565543"

x = txt.isnumeric()   #Syntax:string.isnumeric()

print(x)

   #isprintable():
'''
The isprintable() method returns True if all the characters are printable, otherwise False.

Example of none printable character can be carriage return and line feed.
'''

txt = "Hello! Are you #1?"

x = txt.isprintable()   #Syntax:string.isprintable()

print(x)

   #isspace():
'''
The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.

'''

txt = "   "

x = txt.isspace()   #Syntax:string.isspace()

print(x)

   #istitle():
'''
The istitle() method returns True if all words in a text start with a upper case letter, 
AND the rest of the word are lower case letters, otherwise False.

Symbols and numbers are ignored.
'''
txt = "Hello, And Welcome To My World!"

x = txt.istitle()    #Syntax:string.istitle()

print(x)

   #isupper():
'''
The isupper() method returns True if all the characters are in upper case, otherwise False.

Numbers, symbols and spaces are not checked, only alphabet characters.
'''

txt = "THIS IS NOW!"

x = txt.isupper()  #string.isupper()

print(x)

   #join():
'''
The join() method takes all items in an iterable and joins them into one string.

A string must be specified as the separator.
'''

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)   #Syntax:string.join(iterable)

print(x)

   #ljust():
'''
The ljust() method will left align the string, using a specified character (space is default) as the fill character.

'''

txt = "banana"

x = txt.ljust(20)   #Syntax:string.ljust(length, character)

print(x, "is my favorite fruit.")

   #lower():
'''
The lower() method returns a string where all characters are lower case.

 Symbols and Numbers are ignored.
'''

txt = "Hello my FRIENDS"

x = txt.lower()   #Syntax:string.lower()

print(x)

   #lstrip():
'''The lstrip() method removes any leading characters (space is the default leading character to remove)'''

txt = "     banana     "

x = txt.lstrip()   #Syntax:string.lstrip(characters)

print("of all fruits", x, "is my favorite")

  
   #maketrans():
'''The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
'''

txt = "Hello Sam!"

mytable = str.maketrans("S", "P")   #Syntax:str.maketrans(x, y, z)

print(txt.translate(mytable))

   #partition():
'''
The partition() method searches for a specified string, and splits the string into a tuple containing three elements.

The first element contains the part before the specified string.

The second element contains the specified string.

The third element contains the part after the string.
'''

txt = "I could eat bananas all day"

x = txt.partition("bananas")   #Syntax:string.partition()

print(x)

   #replace():
'''The replace() method replaces a specified phrase with another specified phrase.'''

txt = "I like bananas"

x = txt.replace("bananas", "apples")   #Syntax:string.replace(oldvalue, newvalue, count)

print(x)
#####
txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)

   #rfind():
'''
The rfind() method finds the last occurrence of the specified value.

The rfind() method returns -1 if the value is not found.

The rfind() method is almost the same as the rindex() method. See example below.
'''

txt = "Mi casa, su casa."

x = txt.rfind("casa")   #string.rfind(value, start, end)

print(x)

  #rindex():
'''
The rindex() method finds the last occurrence of the specified value.

The rindex() method raises an exception if the value is not found.

The rindex() method is almost the same as the rfind() method. See example below.
'''

txt = "Mi casa, su casa."

x = txt.rindex("casa")   #Syntax:string.rindex(value, start, end)

print(x)

   #rjust():
'''The rjust() method will right align the string, using a specified character (space is default) as the fill character.'''

txt = "banana"

x = txt.rjust(20)   #syntax:string.rjust(length, character)

print(x, "is my favorite fruit.")


   #rpartition():
'''
The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.

The first element contains the part before the specified string.

The second element contains the specified string.

The third element contains the part after the string.

'''

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")   #Syntax:string.rpartition(value)

print(x)


   #rsplit():
'''
The rsplit() method splits a string into a list, starting from the right.

If no "max" is specified, this method will return the same as the split() method.

'''

txt = "apple, banana, cherry"

x = txt.rsplit(", ")   #Syntax:string.rsplit(separator, maxsplit)

print(x)
#####
txt = "apple, banana, cherry"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)

print(x)


   #rstrip():
'''
The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.

'''

txt = "     banana     "

x = txt.rstrip()    #Syntax:string.rstrip(characters)

print("of all fruits", x, "is my favorite")


   #split():
'''
The split() method splits a string into a list.

You can specify the separator, default separator is any whitespace.
'''

txt = "welcome to the jungle"

x = txt.split()   #Syngtax:string.split(separator, maxsplit)

print(x)

   #splitlines();
'''The splitlines() method splits a string into a list. The splitting is done at line breaks.'''

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()   #Syntax:string.splitlines(keeplinebreaks)

print(x)

   #startswith():
'''The startswith() method returns True if the string starts with the specified value, otherwise False.'''

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

   #strip():
'''
The strip() method removes any leading (spaces at the beginning) and trailing 
(spaces at the end) characters (space is the default leading character to remove)
'''
txt = "     banana     "

x = txt.strip()   #Syntax:string.strip(characters)

print("of all fruits", x, "is my favorite")


    #swapcase():
'''The swapcase() method returns a string where all the upper case letters are lower case and vice versa.'''

txt = "Hello My Name Is PETER"

x = txt.swapcase()    #Syntax:string.swapcase()

print(x)

   #title():
'''
The title() method returns a string where the first character in every word is upper case. Like a header, or a title.

If the word contains a number or a symbol, the first letter after that will be converted to upper case.
'''

txt = "Welcome to my world"

x = txt.title()    #Syntax:string.title()

print(x)

   #translate():
'''
The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.

Use the maketrans() method to create a mapping table.

If a character is not specified in the dictionary/table, the character will not be replaced.

If you use a dictionary, you must use ascii codes instead of characters.
'''

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"    #Syntax:string.translate(table)
print(txt.translate(mydict))

   #upper():
'''
The upper() method returns a string where all characters are in upper case.

 Symbols and Numbers are ignored.
'''

txt = "Hello my friends"

x = txt.upper()    #Syntax:string.upper()

print(x)

   #zfill():
'''
The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.

If the value of the len parameter is less than the length of the string, no filling is done.
'''

txt = "50"

x = txt.zfill(10)   #Syntax:string.zfill(len)

print(x)

