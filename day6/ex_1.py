# adding two zeros after each positive int of a list containing n elements 

def add_zeros(arr):
    new_arr = []
    for i in arr:
        new_arr.append(i)
        if i > 0:
            new_arr.extend([0, 0])
    return new_arr


n = int(input("Enter number of elements : "))
input_arr = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
 
print("\nThe original list is: ", input_arr)
print("The list after adding the zeros: ", add_zeros(input_arr))