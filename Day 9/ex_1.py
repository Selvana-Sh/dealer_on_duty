def flatten_list(_list):
    flattened_list = []
    for item in _list:
        if isinstance(item, list): # checks if item is a list itself
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = flatten_list(list_of_lists)
print(flattened_list)