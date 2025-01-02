# # mean is the sum of all numbers / count of numbersa = [9, 8, 3, 2, 5, 15]# calculate the median and print it

# import numpy
# numbers = [9,8,3,2,5,15]

# mean = sum(numbers)/len(numbers)

# print(mean)

a = 3968

units = ["","one","two","three"]
teens = ["ten","elevan","twelve","thirteen"]
tens = ["tewnty", "thirty", "forty"]
thousands = ["", "thousand"]

def num_to_word(num):
    if num == 0:
        return "zero"
    words = ""

    if num >= 1000:
        words += units[num//1000] + " thousand"
        num %= 1000

    if num >= 100:
        words += units[num//100] + " hundred"
        num = num % 100
        if num > 0:
            words += "and "

    if 



