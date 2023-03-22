# compare two string and return number of matching characters

def matches(str1, str2):
    count = 0
    for char in str1:
        if char in str2:
            count += 1
    return count

str1 = "path"
str2 = "python"
print(matches(str1, str2))  