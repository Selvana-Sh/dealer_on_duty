# create a new list composed of elements with odd orders from list1 and elements with even order from list2.

def odd_even_order(list1, list2):
    new_list = []
    for i in range(len(list1)):
        if i % 2 == 1: # odd indexes of list1
            new_list.append(list1[i])
    for i in range(len(list2)):
        if i % 2 == 0: # even indexes of lis2
            new_list.append(list2[i])
    return new_list

li1 = [1, 2, 3, 4]
li2 = ['a', 'b', 'c', 'd']
print(odd_even_order(li1, li2))