# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with places after the decimal.


def plusMinus(arr):
    plus = 0
    zero = 0
    minus = 0

    for val in arr:
        if val > 0:
            plus += 1
        elif val == 0:
            zero += 1
        elif val < 0:
            minus += 1

    print(f"{plus/len(arr):.6f}")
    print(f"{minus/len(arr):.6f}")
    print(f"{zero/len(arr):.6f}")


print(plusMinus([1, 1, 0, -1, -1]))
