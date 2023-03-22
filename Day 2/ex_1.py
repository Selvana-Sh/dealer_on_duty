str = input("Enter some characters: ")

# string reversed func
def reverse_str(str):
    return str[::-1]

# check if the string is empty
if len(str) == 0:
    print("str not found")
else:
# total number of characters
    print(len(str))

# str repeated 10 times
    _10_times_str = str * 10
    print(_10_times_str)

# first char of str
    first_char = str[0]
    print(first_char)

# first 3 chars of str
    three_chars = str[0:3]
    print(three_chars)

# last 3 chars of str
    last_three_chars = str[-3:]
    print(last_three_chars)

# string reversed 
    backward = reverse_str(str)
    print(backward)