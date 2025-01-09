def reverseBits(n: int):
    reversed_bin = ""
    while n > 0:
        remainder = n % 2
        reversed_bin += str(remainder)
        n = n // 2
    return int(reversed_bin, 2)


print(reverseBits(10))
