def minimumSum(nums):
    min_sum = float("inf")
    left_min = nums[0]
    left_min_idx = 0

    for i in range(1, len(nums) - 1):
        if nums[i] < left_min:
            left_min = nums[i]

        if left_min < nums[i]:
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    peak_sum = left_min + nums[i] + nums[j]
                    if peak_sum < min_sum:
                        min_sum = peak_sum

    return -1 if min_sum == float("inf") else min_sum


print(minimumSum([5, 4, 8, 7, 10, 2]))
