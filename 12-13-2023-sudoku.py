def _getRowData(sudoku):
    rows = {}

    for row in range(0, 9):
        rows[row] = set()
        for col in range(0, 9):
            if sudoku[row][col] > 0:
                rows[row].add(sudoku[row][col])

    return rows


def _getColData(sudoku):
    cols = {}

    for col in range(0, 9):
        cols[col] = set()
        for row in range(0, 9):
            if sudoku[row][col] > 0:
                cols[col].add(sudoku[row][col])

    return cols


def _mapQuandrant(row, col):
    groupMapper = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3}

    quadMapper = {
        1.1: 1,
        1.2: 2,
        1.3: 3,
        2.1: 4,
        2.2: 5,
        2.3: 6,
        3.1: 7,
        3.2: 8,
        3.3: 9,
    }

    rowGroup = groupMapper[row]
    colGroup = groupMapper[col]
    location = float(f"{rowGroup}.{colGroup}")
    quadrant = quadMapper[location]
    return quadrant


def _getQuadrantData(sudoku):
    quadrants = {}

    for quadrant in range(1, 10):
        quadrants[quadrant] = set()

    for row in range(0, 9):
        for col in range(0, 9):
            if sudoku[row][col] > 0:
                quadrants[_mapQuandrant(row, col)].add(sudoku[row][col])

    return quadrants


def _canAddtoRow(rowData, row, testNum):
    return testNum not in rowData[row]


def _canAddtoCol(colData, col, testNum):
    return testNum not in colData[col]


def _canAddtoQuadrant(quadrantData, row, col, testNum):
    quadrant = _mapQuandrant(row, col)
    return testNum not in quadrantData[quadrant]


def solveSudoku(sudoku):
    rowData = _getRowData(sudoku)
    colData = _getColData(sudoku)
    quadrantData = _getQuadrantData(sudoku)

    for row in range(0, 9):
        for col in range(0, 9):
            if sudoku[row][col] == 0:
                for i in range(1, 10):
                    if (
                        _canAddtoRow(rowData, row, i)
                        and _canAddtoCol(colData, col, i)
                        and _canAddtoQuadrant(quadrantData, row, col, i)
                    ):
                        sudoku[row][col] = i
                        rowData[row].add(i)
                        colData[col].add(i)
                        quadrantData[_mapQuandrant(row, col)].add(i)
                        if solveSudoku(sudoku) == True:
                            return True
                        sudoku[row][col] = 0
                        rowData[row].remove(i)
                        colData[col].remove(i)
                        quadrantData[_mapQuandrant(row, col)].remove(i)
                return False

    return True


board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
import time

start = time.time()
a = solveSudoku(board)

for row in board:
    print(*row)

print("time =", time.time() - start)
