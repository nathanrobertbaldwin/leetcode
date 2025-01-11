# Car Fleet

# There are n cars traveling to the same destination on a one-lane highway.

# You are given two arrays of integers position and speed, both of length n.

#     position[i] is the position of the ith car (in miles)
#     speed[i] is the speed of the ith car (in miles per hour)

# The destination is at position target miles.

# A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

# A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

# If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

# Return the number of different car fleets that will arrive at the destination.


# Example 1:

# Input: target = 10, position = [1,4], speed = [3,2]

# Output: 1

# Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

# Example 2:

# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

# Output: 3

# Explanation: The cars starting at 4 and 7 become a fleet at position 10.
# The cars starting at 1 and 0 never catch up to the car ahead of them.
# Thus, there are 3 car fleets that will arrive at the destination.

# Solution: The below solution calculates arrival times for all cars in reverse sorted order
# of their starting position. If a car in front is slower than a car behind, the car behind will have to wait.
# The crux of the problem is recognizing that the cars need to be sorted in this reverse order.
# Complexity: O(n ^ 2)

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortPositions = []
        for i in range(len(position)):
            sortPositions.append((position[i], speed[i]))

        sortPositions.sort(reverse=True)

        arrivalTimes = []
        for i in range(len(sortPositions)):
            arrivalTimes.append((target - sortPositions[i][0]) / sortPositions[i][1])

        for i in range(1, len(arrivalTimes)):
            if arrivalTimes[i] < arrivalTimes[i - 1]:
                arrivalTimes[i] = arrivalTimes[i - 1]

        fleets = len(set(arrivalTimes))
        return fleets


# target = 10
# position = [1, 4]
# speed = [3, 2]
# print(Solution.carFleet(None, target, position, speed))  # 1

# target = 10
# position = [4, 1, 0, 7]
# speed = [2, 2, 1, 1]
# print(Solution.carFleet(None, target, position, speed))  # 3

target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
# 3

print(Solution.carFleet(None, target, position, speed))  # 3
