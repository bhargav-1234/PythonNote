# try:
#     x =int(input("What is x ?"))
#     print(f"x is {x}")

# except ValueError:
#     print("x is not an integer")

#--------------------------------- #

try:
    y = int(input("What is y?"))

except ValueError:
    print("y is not an integer")

else:   # to aviod any other errors we use else
    print(f"y is {y}")


