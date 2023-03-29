# Write a program that generates a list of 20 random numbers between 1 and 100.

import random
my_list = []
i = 0

while i < 20:
    my_list.append(random.randint(1, 100))
    i += 1

# print the list.
print("The list is: ", my_list)

# print the average of the elements in the list.
av = sum(my_list)/ len(my_list)
print("The average of the list is: ", av)

# print the largest and smallest values in the list.
l = max(my_list)
s = min(my_list)
print("The largest value of the list is: ", l)
print("The smallest value of the list is: ", s)

# print the second largest and second smallest entries in the list.
sorted_list = sorted(my_list)
l2 = sorted_list[-2]
s2 = sorted_list[1]
print("The second largest number in the list is: ", l2)
print("The second smallest number in the list is: ", s2)

# print how many even numbers are in the list.
count = 0
for i in range(len(my_list)):
    if i % 2 == 0:
        count += 1
    i+=1
print(f'There is {count} even numbers in the list')
