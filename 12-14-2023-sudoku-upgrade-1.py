# boolean matrix [9 rows][10 values (0 waste plus 1-9)]
# if number 5 is in row 7
# checkrow[7][5] = True
# if number 5 is in row 4
# checkrow[4][5] = True
# if numbers 2,3,5 are in row 0
# checkrow[0] = False, False,  True,  True,  False,  True,  False,  False,  False,  False,


# row,col  = 2,7 -> 2?
# magic formula -> quadrant_number
#  0    1    2

#  3    4    5

#  6    7    8


# row 012 // 3 = 0
# row 345 //3 = 1
# row 678 //3 = 2

# col 012 = 0
# col 345 = 1
# col 678 = 2


checkrow = [[False for i in range(10)] for _ in range(9)]
checkcol = [[False for i in range(10)] for _ in range(9)]
checkquadrant = [[False for i in range(10)] for _ in range(9)]


def get_quadrant_number(row, col):
    return (row // 3) * 3 + (col // 3)


def _does_i_exist_in_quadrant(quadrant_number, testNum):
    return checkquadrant[quadrant_number][testNum]


def _getRowData(sudoku):
    for row in range(0, 9):
        for value in sudoku[row]:
            if value != 0:
                checkrow[row][value] = True


def _getColData(sudoku):
    for row in range(0, 9):
        for col in range(0, 9):
            if sudoku[row][col] != 0:
                checkcol[col][sudoku[row][col]] = True


def _does_i_exist_in_row(row, testNum):
    return checkrow[row][testNum]


def _does_i_exist_in_col(col, testNum):
    return checkcol[col][testNum]


count = 0


def solveSudoku(start_from_row, sudoku):
    global count
    count += 1
    if count % 20000 == 0:
        print(count)
        for i in sudoku:
            print(*i)
        print()

    for row in range(start_from_row, 9):
        for col in range(0, 9):
            if sudoku[row][col] == 0:
                quadrant_number = get_quadrant_number(row, col)
                for i in range(1, 10):
                    if (
                        _does_i_exist_in_row(row, i) == False
                        and _does_i_exist_in_col(col, i) == False
                        and _does_i_exist_in_quadrant(quadrant_number, i) == False
                    ):
                        sudoku[row][col] = i
                        # rowData[row].add(i)
                        checkrow[row][i] = True
                        checkcol[col][i] = True
                        checkquadrant[quadrant_number][i] = True
                        if solveSudoku(row, sudoku) == True:
                            return True
                        sudoku[row][col] = 0
                        checkrow[row][i] = False
                        checkcol[col][i] = False
                        checkquadrant[quadrant_number][i] = False

                return False

    return True


board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def _getQuadrantData(board):
    for row in range(0, 9):
        for col in range(0, 9):
            if board[row][col] != 0:
                quadrant_number = get_quadrant_number(row, col)
                checkquadrant[quadrant_number][board[row][col]] = True


import time

start = time.time()
_getRowData(board)
_getColData(board)
_getQuadrantData(board)


a = solveSudoku(0, board)

for row in board:
    print(*row)

print("time =", time.time() - start)

# dynamic programming ALMOST ALWAYS uses memoization or tabulation??

# memoization is sometimes and sometimes not, used with DP

# memoization is independent from DP, it can exist on its own

# THIS SUDOKU for checkrow uses memoization


# available coins 1, 2, 5

# compute 12?

# dp[7] + 5
# dp[10] + 2
# dp[11] + 1


# compute 13?

# dp[8] + 5
# dp[11] + 2
# dp[12] + 1

# 1 + 2 + 5
# 1 +1 +1 +5
# 2 +2  +2 +2
# for me to get to answer[40] , i need answer[39]

# for me to get to answer[39] , i need answer[38]
