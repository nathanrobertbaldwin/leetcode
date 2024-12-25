class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = []

        running_sum = 0

        for n in nums:
            running_sum += n
            self.sums.append(running_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - self.sums[left - 1] if left > 0 else self.sums[right]
