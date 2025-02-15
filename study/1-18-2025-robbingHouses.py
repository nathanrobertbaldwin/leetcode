from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        d = [nums[0], nums[1]]
        for i in range(2, len(nums)):
            if i == 2:
                d.append(nums[i] + nums[i - 2])
            else:
                d.append(max(d[i - 3] + nums[i], d[i - 2] + nums[i]))

        return max(d[-1], d[-2])

        #  0, 1, 2, 3, 4


print(Solution.rob(None, nums=[5, 1, 2, 10, 6, 2, 7, 9, 3, 1]))  # 27
