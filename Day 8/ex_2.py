# find the missing int in an array from 1 to n

def missing_int(arr):
    
    # number of elements
    n = len(arr) + 1
    
    # what the sum is supposed to be
    total_sum = (n * (n+1)) // 2
    
    # actual sum of arr
    arr_sum = sum(arr)

    _int = total_sum - arr_sum
    
    return _int

my_list = [1, 2, 4, 5, 6]
print(missing_int(my_list))