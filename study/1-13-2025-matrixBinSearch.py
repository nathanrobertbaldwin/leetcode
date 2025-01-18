from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = False
        # search for row with binSearch
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        # search row for target with binSearch
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (right + left) // 2
            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                res = True
                break

        return res


matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target = 10
print(Solution.searchMatrix(None, matrix, target))  # true

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
print(Solution.searchMatrix(None, matrix, target))  # false
