
def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    str_vowels = [char for char in s if char in vowels]

    reverse_vowels = str_vowels[::-1]

    s_list = list(s)

    reverse_vowels_it = iter(reverse_vowels)

    for i,char in enumerate(s_list):
        if char in vowels:
            s_list[i] = next(reverse_vowels_it)

    return ''.join(s_list)

input = 'orange'
out = reverse_vowels(input)
print(out)
