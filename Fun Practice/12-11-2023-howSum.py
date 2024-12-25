# def howSum(targetSum, nums, currCombo=[]):
#     if targetSum == 0:
#         memo[target]
#         return currCombo

#     # testing targetSum < 0 will terminate any recursion where the sum currCombo
#     # is less than zero.
#     if targetSum < 0:
#         return []

#     # We've already passed targetSum test.
#     # We continue testing.
#     # What do we do if we don't find a solution?
#     # We get to the end of the for loop, and the function doesn't have any return,
#     # so that call returns none.
#     for num in nums:
#         combo = howSum(targetSum - num, nums, [*currCombo, num])
#         if len(combo) > 0:
#             return combo

#     return []


# print(howSum(12, [5, 8, 9]))


def howSum(targetSum, nums, currCombo=[], memo={}):
    if targetSum in memo:
        return memo[targetSum]

    if targetSum < 0:
        memo[targetSum] = []
        return memo[targetSum]

    for num in nums:
        if targetSum - num == 0:
            memo[targetSum] = [*currCombo, num]
            return memo[targetSum]

        memo[targetSum] = howSum(targetSum - num, nums, [*currCombo, num], memo)

        if len(memo[targetSum]) > 0:
            return memo[targetSum]

    return []


print(howSum(0, [3, 5, 7]))
