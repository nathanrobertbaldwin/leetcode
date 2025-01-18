from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                res = mid
                break

        return res


nums = [-1, 0, 2, 4, 6, 8]
target = 4
print(Solution.search(None, nums, target))  # 3

nums = [-1, 0, 2, 4, 6, 8]
target = 3
print(Solution.search(None, nums, target))  # -1
