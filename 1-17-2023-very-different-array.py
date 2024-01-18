# Petya has an array ai of n integers. His brother Vasya became envious and decided
# to make his own array of n integers.

# To do this, he found m # integers bi (m≥n), and now he wants
# to choose some n integers of them and arrange them in a
# certain order to obtain an array ci of length n

# To avoid being similar to his brother, Vasya wants to make his array as
# different as possible from Petya's array.
# Specifically, he wants the total difference D=∑ni=1|ai−ci|
# to be as large as possible.

# Help Vasya find the maximum difference D he can obtain.

# Input

# Each test consists of multiple test cases. The first line contains a single integer t
# (1≤t≤100) — the number of test cases. This is followed by a description of the test cases.

# The first line of each test case contains two integers n
# and m (1≤n≤m≤2⋅105).

# The second line of each test case contains n
# integers ai (1≤ai≤109). The third line of each test case contains m integers bi (1≤bi≤109).

# It is guaranteed that in a test, the sum of m
# over all test cases does not exceed 2⋅105

# Output

# For each test case, output a single integer — the maximum total difference D
# that can be obtained

# want to maximize the difference at each index, which will max the sum of the diffs

from collections import Counter


def maxDifference(a, b):
    a.sort()
    b.sort(reverse=True)

    max_diff = 0

    left = 0
    a_right = len(a) - 1
    b_right = len(b) - 1

    while left <= a_right:
        if abs(a[left] - b[left]) >= abs(a[a_right] - b[b_right]):
            max_diff += abs(a[left] - b[left])
            left += 1
        else:
            max_diff += abs(a[a_right] - b[b_right])
            a_right -= 1
            b_right -= 1

    return max_diff


arr1 = [1, 2, 4, 6]
arr2 = [7, 5, 3, 3, 2, 1]

print(maxDifference(arr1, arr2))
