# Quadrant Mapping

quadrant_rows = {
    0: [0, 1, 2],
    1: [0, 1, 2],
    2: [0, 1, 2],
    3: [3, 4, 5],
    4: [3, 4, 5],
    5: [3, 4, 5],
    6: [6, 7, 8],
    7: [6, 7, 8],
    8: [6, 7, 8],
}

quadrant_cols = {
    0: [0, 1, 2],
    1: [3, 4, 5],
    2: [6, 7, 8],
    3: [0, 1, 2],
    4: [3, 4, 5],
    5: [6, 7, 8],
    6: [0, 1, 2],
    7: [3, 4, 5],
    8: [6, 7, 8],
}

# Input

board = [
    [0, 0, 7, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 2, 0, 8, 0, 0],
    [0, 2, 3, 4, 8, 7, 0, 5, 0],
    [0, 0, 8, 5, 0, 0, 1, 0, 0],
    [0, 1, 9, 0, 0, 0, 2, 4, 0],
    [0, 0, 4, 0, 0, 3, 6, 0, 0],
    [0, 5, 0, 2, 3, 6, 7, 9, 0],
    [4, 0, 2, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 0],
]

# Board Preprocessing

row_data = [[False for i in range(10)] for _ in range(9)]
col_data = [[False for i in range(10)] for _ in range(9)]
quadrant_data = [[False for i in range(10)] for _ in range(9)]


def _get_row_data(sudoku):
    for row in range(0, 9):
        for value in sudoku[row]:
            if value != 0:
                row_data[row][value] = True


def _get_col_data(sudoku):
    for row in range(0, 9):
        for col in range(0, 9):
            if sudoku[row][col] != 0:
                col_data[col][sudoku[row][col]] = True


def _get_quadrant_number(row, col):
    return (row // 3) * 3 + (col // 3)


def _get_quadrant_data(board):
    for row in range(0, 9):
        for col in range(0, 9):
            if board[row][col] != 0:
                quadrant_number = _get_quadrant_number(row, col)
                quadrant_data[quadrant_number][board[row][col]] = True


# Retrieve Preprocessed Row, Col, and Quadrant Info


def _i_in_row(row, testNum):
    return row_data[row][testNum]


def _i_in_col(col, testNum):
    return col_data[col][testNum]


def _i_in_quadrant(quadrant_number, testNum):
    return quadrant_data[quadrant_number][testNum]


# Add Deterministic Values Using Set Differences


def _make_set_diff_changes(quadrant):
    changed = False

    rows = quadrant_rows[quadrant]
    cols = quadrant_cols[quadrant]

    for i in range(1, 10):
        if _i_in_quadrant(quadrant, i) == True:
            continue

        num_map = set(
            (row, col) for row in rows for col in cols if board[row][col] == 0
        )

        difference = set()

        for row in rows:
            if _i_in_row(row, i) == True:
                for coordinate in num_map:
                    if coordinate[0] == row:
                        difference.add(coordinate)

        for col in cols:
            if _i_in_col(col, i) == True:
                for coordinate in num_map:
                    if coordinate[1] == col:
                        difference.add(coordinate)

        num_map.difference_update(difference)

        if len(num_map) == 1:
            changed = True

            coordinate = num_map.pop()
            row = coordinate[0]
            col = coordinate[1]

            board[row][col] = i

            row_data[row][i] = True
            col_data[col][i] = True
            quadrant_data[_get_quadrant_number(row, col)][i] = True

    return changed


def solve_deterministic_numbers(sudoku):
    for quadrant in range(0, 9):
        changed = _make_set_diff_changes(quadrant)
        if changed == True:
            solve_deterministic_numbers(board)


# Solve Remaining Non-Deterministic Sudoku Using Recursion


def solve_remaining_recursive(sudoku, start_row=0):
    for row in range(start_row, 9):
        for col in range(0, 9):
            if sudoku[row][col] == 0:
                quadrant_number = _get_quadrant_number(row, col)
                for i in range(1, 10):
                    if (
                        _i_in_row(row, i) == False
                        and _i_in_col(col, i) == False
                        and _i_in_quadrant(quadrant_number, i) == False
                    ):
                        sudoku[row][col] = i
                        row_data[row][i] = True
                        col_data[col][i] = True
                        quadrant_data[quadrant_number][i] = True

                        if solve_remaining_recursive(sudoku, row) == True:
                            return True

                        sudoku[row][col] = 0
                        row_data[row][i] = False
                        col_data[col][i] = False
                        quadrant_data[quadrant_number][i] = False

                return False

    return True


import time

start = time.time()

_get_row_data(board)
_get_col_data(board)
_get_quadrant_data(board)

solve_deterministic_numbers(board)
solve_remaining_recursive(board)

for row in board:
    print(*row)

print("time =", time.time() - start)
