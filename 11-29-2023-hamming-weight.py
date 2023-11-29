def hammingWeight(num):
        binary = bin(num)[2:]
        count = 0
        for digit in binary:
            count += int(digit)
        return count


print(hammingWeight(255))
