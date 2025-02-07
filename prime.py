# lower = int(input("Enter the lower value:"))
# upper = int(input("Enter the upper value:"))
# for number in range(lower,upper+1):
#     if number>1:
#         for i in range(2,number):
#             if (number%i)==0:
#                 break
#         else:
#             print(number)
# ###########
# for i in range(3):
#     print("meow")
##########################
# def main():
#     meow(3)

# def meow(n):
#     for _ in range(n):
#         print("meow")
    
# main()

# for number in range(2, 100):
#     if number  == 0:
#         break
#     else:
#         print(number)

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True

# # Print prime numbers up to a given limit
# # limit = int(input("Enter limit: "))
# for num in range(2, 10):
#     if is_prime(num):
#         print(num)

### ---- Most popular interview Question ---- ###
# def prime(num):
#     if num<=1:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#          return False
#     return True
# for num in range(2,10):
#    if prime(num):
#        print(num)
def prime(num):
    if num <=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
for num in range(2,20):
    if prime(num):
     print(num)