# 11. Container With Most Water
# Medium
# Topics
# Companies
# Hint

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Notes: A greedy algorithm is an algorithm that solves a larger problem by "greedily" choosing the
# optimal solution for each sub problem in a set of sub problems, and the optimal solution
# sub problems is the solution of the larger problems.
# i.e. A problem can be solved with a greedy algorithm if:
# the problem can be divided into sub problems.
# The solution to the problem itself is contained
# in the set of solutions to the sub problem.

# Problem: We have an array of heights. Which two heights produces the largest container?
# Sub problems: Given a single container side, which choice of other side produces the max volume?
# The solution to the problem is the largest solution to the sub problems.


def maxArea(height):
    largestArea = 0

    left = 0
    right = len(height)

    


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
