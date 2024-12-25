def inversionCounter(matrix):
    inversions = 0

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            currVal = matrix[row][col]
            for i in range(row, len(matrix)):
                for j in range(col, len(matrix)):
                    if currVal > matrix[i][j]:
                        inversions += 1

    return inversions


print(inversionCounter([[3, 1, 2], [2, 3, 1], [1, 2, 3]]))
