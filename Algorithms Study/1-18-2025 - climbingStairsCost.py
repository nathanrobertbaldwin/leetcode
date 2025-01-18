# Min Cost Climbing Stairs

# You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.

# You may choose to start at the index 0 or the index 1 floor.

# Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.

# Example 1:

# Input: cost = [1,2,3]

# Output: 2

# Explanation: We can start at index = 1 and pay the cost of cost[1] = 2 and take two steps to reach the top. The total cost is 2.

# Example 2:

# Input: cost = [1,2,1,2,1,1,1]

# Output: 4

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = [0, 0]

        i = 2
        while i < len(cost) + 1:
            d.append(min(d[i - 2] + cost[i - 2], d[i - 1] + cost[i - 1]))
            i += 1

        return d[-1]


print(Solution.minCostClimbingStairs(None, [1, 2, 3]))  # 2
print(Solution.minCostClimbingStairs(None, [1, 2, 1, 2, 1, 1, 1]))  # 4
