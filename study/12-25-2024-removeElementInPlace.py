# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

#     Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
#     Return k.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }

# If all assertions pass, then your solution will be accepted.


# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

from typing import List


# Solution: Scan nums to find instance of target. Scan nums from end to find an instance of a number that isn't the target. Swap.
# Complexity: n
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        k = 0

        found = False
        while i <= j:
            while j >= 0 and found == False and nums[j] == val:
                j -= 1
            found = True
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
                found = False
            else:
                i += 1
                k += 1

        return k


# 2. Make a temp buffer. Put els from nums that aren't target in temp. Copy temp back to nums.

nums = [3, 2, 2, 3]
val = 3
print(Solution.removeElement(None, nums, val))
print(nums)
# Output: 2, nums = [2,2,_,_]

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(Solution.removeElement(None, nums, val))
print(nums)
# Output: 5, nums = [0,1,4,0,3,_,_,_]

nums = [1]
val = 1
print(Solution.removeElement(None, nums, val))
print(nums)
# Output: 2, nums = [2,2,_,_]
