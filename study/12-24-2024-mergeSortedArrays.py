from typing import List


# Solution: Create a temp buffer and copy the nums1 into it. Merge both arrays back to nums1.
# Complexity: n + (m + n)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Copy els of nums1 to a temp buffer
        t = []
        for i in range(0, m):
            t.append(nums1[i])

        i = 0
        j = 0
        # Merge the two sorted arrays back to nums1 in sorted order.
        while i < m and j < n:
            if t[i] <= nums2[j]:
                nums1[i + j] = t[i]
                i += 1
            else:
                nums1[i + j] = nums2[j]
                j += 1

        while i < m:
            nums1[i + j] = t[i]
            i += 1

        while j < n:
            nums1[i + j] = nums2[j]
            j += 1


# Solution: Copy els of nums2 into the remaining space of nums1. Sort nums1.
# Complexity: n + (m + n)log(m + n)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m
        j = 0

        while i < (m + n):
            nums1[i] = nums2[j]
            i += 1

        nums1.sort()


# # Solution: Use two pointers to find the insert position for each next element of nums2 into nums1.
# # Complexity: m*n
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # ptr at end of nums2
        j = n - 1

        # for each el of nums2
        while j >= 0:
            # create a new ptr to the end of nums1 + 1.
            i = m
            # while i is still in bounds and el of nums2 is less than el of nums1
            while i > 0 and nums2[j] < nums1[i - 1]:
                # copy the el to the left of the ptr at i (i - 1) to i
                nums1[i] = nums1[i - 1]
                # decrement i
                i -= 1
            # at the end of the loop, ptr i is now located at the correct insert position.
            nums1[i] = nums2[j]
            # increment m to denote additional el added to nums1.
            m += 1
            # move ptr j to begin inserting the next el of nums2 into nums1.
            j -= 1


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
print(Solution.merge(None, nums1, m, nums2, n))
print(nums1)


nums1 = [2, 0]
nums2 = [1]
m = 1
n = 1
print(Solution.merge(None, nums1, m, nums2, n))
print(nums1)

nums1 = [0, 0, 0, 0, 0]
nums2 = [1, 2, 3, 4, 5]
m = 0
n = 5
print(Solution.merge(None, nums1, m, nums2, n))
print(nums1)

nums1 = [1]
nums2 = []
m = 1
n = 0
print(Solution.merge(None, nums1, m, nums2, n))
print(nums1)
