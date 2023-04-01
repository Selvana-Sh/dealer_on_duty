def sum_of_digits(n):
    # Keep looping until n is a single-digit number
    while n >= 10:
        # Compute the sum of the digits of n
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n //= 10
        # Update n to the sum of digits
        n = digit_sum
    # Return the final single-digit value
    return n

test_int = int(input("Enter a non-negative integer: "))
print(sum_of_digits(test_int))