from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        testMin = 1
        testMax = max(piles)

        res = testMin
        while testMin <= testMax:
            testRate = (testMin + testMax) // 2
            if Solution.canFinishOnTime(None, piles, testRate, h):
                res = testRate
                testMax = testRate - 1
            else:
                testMin = testRate + 1

        return res

    def canFinishOnTime(self, piles, eatSpeed, h):

        time = 0
        for pile in piles:
            while pile > 0:
                time += 1
                if time > h:
                    return False
                pile -= eatSpeed

        return True


# piles = [1, 4, 3, 2]
# h = 9
# print(Solution.minEatingSpeed(None, piles, h))  # 2

piles = [25, 10, 23, 4]
h = 4
print(Solution.minEatingSpeed(None, piles, h))  # 25
