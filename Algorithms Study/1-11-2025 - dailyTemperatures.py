from typing import List

# Brute Force: The brute force solution uses a nested for loop. The out loop sets a pointer to the current element,
# the inner loop scans ahead of the current element to find the first index where temperatures[index] > temperatures[current element].
# Time complexity: O(n ^ 2)
# Space complexity: O(n)

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         t = temperatures
#         res = [0 for _ in range(len(temperatures))]
#         # start at index 1 and look backwards
#         currIdx = 1
#         s = [(0, t[0])]
#         # while in bounds
#         while currIdx < len(t):
#             # if decreasing
#             if t[currIdx - 1] > t[currIdx]:
#                 # add the index and the value at that index to the stack
#                 s.append((currIdx, t[currIdx]))
#             else:
#                 # if increasing
#                 while len(s) > 0 and s[-1][1] < t[currIdx]:
#                     # pop items off the stack until the stack is empty or until we find a higher value
#                     pastIdx, _ = s.pop()
#                     res[pastIdx] = currIdx - pastIdx
#                 # we are done processing the current index, append it to the stack and continue
#                 s.append((currIdx, t[currIdx]))
#             currIdx += 1

#         return res


# temperatures = [30, 38, 30, 36, 35, 40, 28]
# # [1, 4, 1, 2, 1, 0, 0]

# # temperatures = [22, 21, 20]
# # [0, 0, 0]

# print(Solution.dailyTemperatures(None, temperatures))


# The below uses a stack to move backwards through already visited indices to find
# the first location where the value at that index is greater than the value at the current index.
# We update res as we pop items off the stack in reverse order.
# Time Complexity: Worst case is still O(n ^ 2), best case is O(n)
# Space Complexity: Worst case is O(2n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        res = [0 for _ in range(len(temperatures))]
        # start at index 1 and look backwards
        currIdx = 1
        s = [(0, t[0])]
        # while in bounds
        while currIdx < len(t):
            while len(s) > 0 and s[-1][1] < t[currIdx]:
                # pop items off the stack until the stack is empty or until we find a higher value
                pastIdx, _ = s.pop()
                res[pastIdx] = currIdx - pastIdx
            # we are done processing the current index, append it to the stack and continue
            s.append((currIdx, t[currIdx]))
            currIdx += 1

        return res


temperatures = [30, 38, 30, 36, 35, 40, 28]
# [1, 4, 1, 2, 1, 0, 0]

# temperatures = [22, 21, 20]
# [0, 0, 0]

print(Solution.dailyTemperatures(None, temperatures))
