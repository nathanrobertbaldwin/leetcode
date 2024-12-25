import math


def findRange(nums, target):
    def find_left(nums, target):
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (r + l) // 2
            if target <= nums[m]:
                r = m
            elif target > nums[m]:
                l = m + 1

        return l if nums[l] == target else -1

    def find_right(nums, target):
        l = 0
        r = len(nums) - 1

        while l < r:
            m = math.ceil((r + l) / 2)
            if target < nums[m]:
                r = m - 1
            elif target >= nums[m]:
                l = m

        return r if nums[r] == target else -1

    return [find_left(nums, target), find_right(nums, target)]


print(findRange([5, 7, 7, 8, 8, 10], 8))
