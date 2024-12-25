def integerReplacement(n):
    count = 0
    while n > 1:
        if n == 3:
            count += 2
            return count
        elif n % 2 == 0:
            n = n // 2
            count += 1
        else:
            if ((n + 1) // 2) % 2 == 0:
                n = n + 1
                count += 1
            elif ((n - 1) // 2) % 2 == 0:
                n = n - 1
                count += 1
    return count


print(integerReplacement(3))
