# Climbing Stairs
# Solved

# You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

# Return the number of distinct ways to climb to the top of the staircase.

# Example 1:

# Input: n = 2

# Output: 2

# Explanation:

#     1 + 1 = 2
#     2 = 2

# Example 2:

# Input: n = 3

# Output: 3

# Explanation:

#     1 + 1 + 1 = 3
#     1 + 2 = 3
#     2 + 1 = 3

# Constraints:

#     1 <= n <= 30

# The number of ways to get to position n is equal to the number of ways to get to n - 1
# plus the number of ways to get to n - 2 (since we can take both one step and two steps).


# Brute Force
# Time Complexity: At each recursive step, the brute force solution makes two calls: climbStairs(n - 1) + climbStairs(n -2).
# The recursion terminates at n - 1 or n = 0, yielding a time complexity of 2^n.
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0 or n == 1:
#             return 1
#         return Solution.climbStairs(self, n - 1) + Solution.climbStairs(self, n - 2)


# Memoization
# The brute force solution requires many duplicate calculations.
# We can store the solution for some n in a dictionary. Use the dictionary to retrieve already completed calcs.
class Solution:
    def climbStairs(self, n: int) -> int:
        d = dict()
        d[0] = 1
        d[1] = 1

        def explore(n):
            if n in d:
                return d[n]
            else:
                # this sets the value in the dictionary, but by itself does not return the value
                # to the previous recursive call.
                d[n] = explore(n - 1) + explore(n - 2)
                # required to return the value to the previous recursive call.
                return d[n]

        explore(n)
        return d[n]


# print(Solution.climbStairs(None, 1))
# print(Solution.climbStairs(None, 2))
print(Solution.climbStairs(None, 3))

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         # let the index = num steps
#         d = [1, 1]
#         while len(d) <= n:
#             d.append(d[-1] + d[-2])
#         return d[-1]
