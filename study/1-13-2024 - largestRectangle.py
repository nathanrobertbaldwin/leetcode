from typing import List


# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         largestRectangle = 0
#         for i in range(len(heights)):
#             if heights[i] > largestRectangle:
#                 largestRectangle = heights[i]
#             smallestHeight = heights[i]
#             for j in range(i + 1, len(heights)):
#                 if heights[j] < smallestHeight:
#                     smallestHeight = heights[j]
#                 width = (j - i) + 1
#                 area = smallestHeight * width
#                 if area > largestRectangle:
#                     largestRectangle = area

#         return largestRectangle


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        res = 0
        for i in range(0, len(heights)):
            if len(s) > 0 and heights[i] >= s[-1][1]:
                s.append((i, heights[i]))
            else:
                j = i
                while len(s) > 0 and heights[i] < s[-1][1]:
                    j, height = s.pop()
                    area = (i - j) * height
                    if area > res:
                        res = area

                s.append((j, heights[i]))

        i += 1
        while len(s) > 0:
            j, height = s.pop()
            area = (i - j) * height
            if area > res:
                res = area

        return res


heights = [7, 1, 7, 2, 2, 4]
print(Solution.largestRectangleArea(None, heights))


heights = [1, 3, 7]
print(Solution.largestRectangleArea(None, heights))
