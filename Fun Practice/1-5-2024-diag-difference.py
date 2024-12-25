def diagonalDifference(m):
    diag_right_sum = 0
    row = 0
    col = 0

    while row < len(m):
        diag_right_sum += m[row][col]
        row += 1
        col += 1

    diag_left_sum = 0
    row = 0
    col = len(m) - 1

    while col >= 0:
        diag_left_sum += m[row][col]
        row += 1
        col -= 1

    return abs(diag_right_sum - diag_left_sum)


matrix = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

print(diagonalDifference(matrix))
