def shift_zeros(_list):

    # counting and assigning non-zero elements
    count = 0
    for i in range(len(_list)):
        if _list[i] != 0:
            _list[count] = _list[i]
            count += 1
    
    # filling the zeros
    while count < len(_list):
        _list[count] = 0
        count += 1
    
    return _list

list1 = [0, 1, 0, 0, 3, 132]
print(shift_zeros(list1))
