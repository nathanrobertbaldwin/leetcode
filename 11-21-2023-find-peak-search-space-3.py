def findPeakElement(self, nums: [int]) -> int:
    l = 0
    r = len(nums) - 1

    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        return 0 if nums[0] > nums[1] else 1

    while l + 1 < r:
        m = (l + r) // 2
        if nums[m] < nums[m + 1]:
            l = m
        if nums[m] > nums[m + 1]:
            r = m

    return l if nums[l] > nums[l + 1] else l + 1
