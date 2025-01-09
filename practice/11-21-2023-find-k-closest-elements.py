# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

#     |a - x| < |b - x|, or
#     |a - x| == |b - x| and a < b

import math


def findIdxRange(arr, k, x):
    l = 0
    r = len(arr) - 1

    while l + 1 < r:
        m = (l + r) // 2
        if x <= arr[m]:
            r = m
        elif x > arr[m]:
            l = m

    return [max(0, l - k), l, r, min(len(arr) - 1, r + k)]


# nice!


def findClosestElements(arr: [int], k: int, x: int) -> [int]:
    res = []

    idx_range = findIdxRange(arr, k, x)

    l_bound = idx_range[0]
    l = idx_range[1]
    r = idx_range[2]
    r_bound = idx_range[3]

    while len(res) < k:
        if l < l_bound:
            res.append(arr[r])
            r += 1
        elif r > r_bound:
            res.append(arr[l])
            l -= 1
        elif abs(arr[l] - x) <= abs(arr[r] - x):
            res.append(arr[l])
            l -= 1
        elif abs(arr[l] - x) > abs(arr[r] - x):
            res.append(arr[r])
            r += 1

    res.sort()
    return res


arr = [1, 2, 3, 4, 6]
k = 4
x = 3
# Output: [1,2,3,4]

print(findClosestElements(arr, k, x))
