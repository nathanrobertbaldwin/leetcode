# doesn't work \

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        left = 0
        mid = 1
        right = len(nums) - 1

        while mid < len(nums) - 1:
            # skips dups
            while mid < len(nums) - 2 and nums[mid] == nums[mid + 1]:
                mid += 1

            while left < mid and mid < right:
                # skips dups
                while left < mid - 1 and nums[left] == nums[left + 1]:
                    left += 1

                while right > mid + 1 and nums[right] == nums[right - 1]:
                    right -= 1

                if nums[left] + nums[mid] + nums[right] > 0:
                    right -= 1
                elif nums[left] + nums[mid] + nums[right] < 0:
                    left += 1
                else:
                    res.append([nums[left], nums[mid], nums[right]])
                    left += 1
                    right -= 1

            mid += 1

        return res


nums = [-2, 0, 1, 1, 2]

print(Solution.threeSum(None, nums))
