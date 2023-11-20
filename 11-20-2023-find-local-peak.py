def find_local_peak(nums):
    l = 0
    r = len(nums) - 1

    while l < r:
        mid = (l + r) // 2

        if nums[mid] < nums[l]:
            r = mid
        else:
            l = mid + 1
            
    return nums[r + 1]


# 1. l = 4, r = 6
# 2. l = 4, r = 5,
# 3. l = 5, r = 5


print(find_local_peak([3, 4, 5, 1, 2]))
