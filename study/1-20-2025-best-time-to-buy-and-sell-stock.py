from typing import List
import heapq

# We are looking for some interval defined by i and j, where i < j, and we have
# prices[j] - prices[i] is largest in the array.


# Naive solution: Test all combinations of sell days that come after buy dates.
# Implementation: Nested for loop, where inner for loop starts at current index + 1
# Complexity: O(n ^ 2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > bestProfit:
                    bestProfit = prices[j] - prices[i]

        return bestProfit


# Is it possible to do this in a single for loop?
# - Identifying max and min in the array in a single loop
# doesn't take into account chronology of buy dates/sale dates.
# - Using two pointers to identify some local max and some local min doesn't work,
# since the optimal answer could be somewhere else in the array.
# - Two pointers that move independently of each other doesn't work.
# - Sliding window?


# Better Solution: 1. Skip decreasing intervals, 2. When you find an increasing
# interval, begin scanning for max profit until you find a new low point. 3. Catch
# up the slow pointer.
# O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i = 0

        while i < len(prices) - 1:
            if prices[i] > prices[i + 1]:
                i += 1
            else:
                j = i + 1
                while j < len(prices) and prices[i] <= prices[j]:
                    if prices[j] - prices[i] > res:
                        res = prices[j] - prices[i]
                    j += 1
                i = j

        return res


print(Solution.maxProfit(None, [10, 1, 5, 6, 7, 1]))  # 6
print(Solution.maxProfit(None, [10, 8, 7, 5, 2]))  # 0
print(Solution.maxProfit(None, [10, 1, 10, 6, 7, 1]))  # 9
print(Solution.maxProfit(None, [7, 1, 5, 3, 6, 4]))  # 5
print(Solution.maxProfit(None, [2, 1, 2, 1, 0, 1, 2]))  # 2
