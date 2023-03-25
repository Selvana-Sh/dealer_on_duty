# replace all vowels in a str with '*'

def replace_vowels(string):
    vowels = "aeiouAEIOU"
    res = ""
    for char in string:
        if char in vowels:
            res += "*"
        else:
            res += char
    return res

str = "lol"
print(replace_vowels(str))