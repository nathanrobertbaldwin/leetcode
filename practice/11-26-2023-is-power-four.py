def isPowerOfFour(n):
    sum = 0

    while n > 0:
        base_4_digit = n % 4
        sum += base_4_digit
        n = n // 4

    return sum == 1


print(isPowerOfFour(256))
