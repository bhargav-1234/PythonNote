# #Python User Input:

# #User input:
# '''Python allows for user input.

# That means we are able to ask the user for input.

# The method is a bit different in Python 3.6 than Python 2.7.

# Python 3.6 uses the input() method.

# Python 2.7 uses the raw_input() method.

# The following example asks for the username, and when you entered the username, it gets printed on the screen.
# '''

# #Python 3.6:
# username = input("Enter username:")
# print("Username is: " + username)


# #Python 2.7:
#   #username = raw_input("Enter username:")
#   #print("Username is: " + username)

# #Python stops executing when it comes to the input() function, and continues when the user has given some input.

# name = input("what is your name ? ")
# file = open("names.txt", "w")
# file.write(name)
# file.close()


# name = input("what is your name ? ")
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()


# name = input("what is your name ? ")
# with open("names.txt", "a") as file:
#  file.write(f"{name}\n")


# names = []
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
# for name in sorted(names):
#     print(f"hello,{name}")

# names = []
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
# for name in sorted(names, reverse=True):
#     print(f"hello,{name}")
    

# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")


# email = input("what is your email ? ")
# if "@" in email and "." in email:
#     print("valid")
# else:
#     print("invalid")

import re
email = input("enter your email ? ")

if re.search("..+@..+", email):
    print("valid")
else:
    print("invalid")


