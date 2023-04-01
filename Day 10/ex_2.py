def count_bits(num):
    if num < 0:
        print("Error: Input number must be non-negative.")
    else:
        binary = bin(num)[2:]  # convert num to binary + remove the "0b" prefix
        return binary.count('1')

num = int(input("Enter a non-negative num: "))
print(count_bits(num))