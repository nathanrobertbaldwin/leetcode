from typing import List
import heapq


# Solution: Counts the occurences of the nums in the list, then sorts,
# then picks the top k.
# Complexity: n + nlog(n) + k
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = dict()

#         for num in nums:
#             if num in counter:
#                 counter[num] += 1
#             else:
#                 counter[num] = 1

#         counter = list(sorted(counter.items(), key=lambda item: item[1], reverse=True))

#         res = []
#         for i in range(k):
#             res.append(counter[i][0])

#         return res


# Solution: This solution uses a heap to sort the elements by frequency upon insertion into the heap.
# Complexity: n + nlog(n) + k
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = dict()

#         for num in nums:
#             if num in counter:
#                 counter[num] += 1
#             else:
#                 counter[num] = 1

#         freq = []
#         for num, count in counter.items():
#             heapq.heappush(freq, (-count, num))

#         res = []
#         for i in range(k):
#             res.append(heapq.heappop(freq)[1])

#         return res


# nums = [1, 2, 2, 3, 3, 3]
# k = 2


# Solution: This solution uses bucket sort. First, create a counter map.
# Then, instead of sorting the counter map by internally comparing elements,
# we use buckets in an array. Remember to create an array of buckets
# range(len(nums) + 1), since the 0 bucket will not be used (we cannot have an)
# element in nums that appears 0 times).
# Complexity: n + n + n + k
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counter.items():
            buckets[count].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res


nums = [1, 2, 2, 3, 3, 3]
k = 2
print(Solution.topKFrequent(None, nums, k))
