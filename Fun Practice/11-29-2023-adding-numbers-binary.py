def toBin(num):
    arr = [0] * 32

    if num < 0:
        arr[0] = 1
        num = -num - 1

    digit = 31
    while num > 0:
        arr[digit] = num % 2
        num = num // 2
        digit -= 1

    if arr[0] == 1:
        for i in range(1, 32):
            if arr[i] == 0:
                arr[i] = 1
            elif arr[i] == 1:
                arr[i] = 0

    return arr


def getSum(a, b):
    a_bin = toBin(a)
    b_bin = toBin(b)

    sum = [0] * 32

    carry = 0
    for i in range(31, -1, -1):
        new_digit = a_bin[i] + b_bin[i] + carry

        if new_digit > 1:
            carry = 1
            new_digit -= 2
            sum[i] = new_digit
        else:
            sum[i] = new_digit
            carry = 0

    if sum[0] == 0:
        bin_str = "".join(str(digit) for digit in sum)[1:]
        return int(bin_str, 2)

    if sum[0] == 1:
        for i in range(31, 0, -1):
            if sum[i] == 0:
                sum[i] = 1
            elif sum[i] == 1:
                sum[i] = 0

        bin_str = "".join(str(digit) for digit in sum)[1:]
        return -int(bin_str, 2) - 1


print(getSum(0, -7))
