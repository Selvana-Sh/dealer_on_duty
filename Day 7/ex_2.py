# Convert two lists into one dictionary

#keys = ['Ten', 'Twenty', 'Thirty']
#values = [10, 20, 30] 

keys = input("Enter the keys (separated by space): ").split()
values = input("Enter the values (separated by space): ").split()

dictionary = {}
for i in range(len(keys)):
    dictionary[keys[i]] = values[i]

print(dictionary)