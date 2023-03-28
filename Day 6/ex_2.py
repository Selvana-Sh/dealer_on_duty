# count letters in a str, return a dict of the letters and their frequency

def count_letters(string):
    freq = {}

    for char in string:

        # check if it's a letter
        if not char.isalpha():
            continue

        # increment in case of exising char
        if char in freq:
            freq[char] += 1

        # add the non-exsistent char
        else:
            freq[char] = 1

    return freq


str = input("Enter a string: ")
print("Original str was: ")
print(count_letters(str))