def runningSum(nums):
    runningSum = []
    currSum = 0
    for num in nums:
        currSum += num
        runningSum.append(currSum)

    return runningSum


print(runningSum([1, 2, 3, 4, 5]))
