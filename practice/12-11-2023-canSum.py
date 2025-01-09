def canSum(targetSum, nums, priorSums={}):
    if targetSum == 0:
        return True

    if targetSum < 0:
        return False

    if targetSum in priorSums:
        return priorSums[targetSum]

    for num in nums:
        priorSums[targetSum] = canSum(targetSum - num, nums, priorSums)
        return priorSums[targetSum]


print(canSum(300, [7, 14]))

# time complexity: m levels and n more nodes per level => n * n * n, m times, n**m
# space complexity depends on m