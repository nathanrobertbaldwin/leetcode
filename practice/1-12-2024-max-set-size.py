# 3002. Maximum Size of a Set After Removals
# Medium
# Topics
# Companies
# Hint

# You are given two 0-indexed integer arrays nums1 and nums2 of even length n.

# You must remove n / 2 elements from nums1 and n / 2 elements from nums2. After the removals, you insert the remaining elements of nums1 and nums2 into a set s.

# Return the maximum possible size of the set s.


# Example 1:

# Input: nums1 = [1,2,1,2], nums2 = [1,1,1,1]
# Output: 2
# Explanation: We remove two occurences of 1 from nums1 and nums2. After the removals, the arrays become equal to nums1 = [2,2] and nums2 = [1,1]. Therefore, s = {1,2}.
# It can be shown that 2 is the maximum possible size of the set s after the removals.

# Example 2:

# Input: nums1 = [1,2,3,4,5,6], nums2 = [2,3,2,3,2,3]
# Output: 5
# Explanation: We remove 2, 3, and 6 from nums1, as well as 2 and two occurrences of 3 from nums2. After the removals, the arrays become equal to nums1 = [1,4,5] and nums2 = [2,3,2]. Therefore, s = {1,2,3,4,5}.
# It can be shown that 5 is the maximum possible size of the set s after the removals.


def counter(arr1, arr2):
    combined = arr1 + arr2
    counter = {num: {1: 0, 2: 0} for num in combined}

    for num in arr1:
        counter[num][1] += 1

    for num in arr2:
        counter[num][2] += 1

    return counter


def maximumSetSize(nums1, nums2):
    combined = counter(nums1, nums2)

    half1 = len(nums1) // 2
    half2 = len(nums2) // 2

    removed1 = 0
    removed2 = 0

    # remove shared
    for num in combined:
        while combined[num][1] > 1 and removed1 < half1:
            removed1 += 1
            combined[num][1] -= 1

        while combined[num][2] > 1 and removed2 < half2:
            removed2 += 1
            combined[num][2] -= 1

    for num in combined:
        if removed1 < half1 and combined[num][2] >= 1:
            removed1 += combined[num][1]
            combined[num][1] = 0
        if removed2 < half2 and combined[num][1] >= 1:
            removed2 += combined[num][2]
            combined[num][2] = 0

    to_del = (half1 - removed1) + (half2 - removed2)

    return len(combined.keys()) - to_del


nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [2, 3, 2, 3, 2, 3]

print(maximumSetSize(nums1, nums2))
