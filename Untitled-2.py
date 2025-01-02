
def recursive(str, index):
    if index == len(str):
        print("No capital letters")
    if str[index].isupper():
        return str[index]
    return recursive(str, index+1)


str = ""
cap = recursive(str, index=0)


print(cap)
                
