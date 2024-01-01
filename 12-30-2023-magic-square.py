# We define a magic square to be an matrix of distinct positive integers
# from 1 - 9 to where the sum of any row, column, or diagonal of length
# is always equal to the same number: the magic constant.

# You will be given a matrix of integers in the inclusive range 1 - 9.
# We can convert any digit to any other digit in the range at cost of |a - b|
# Given m convert it into a magic square at minimal cost. Print this cost on a new line.

# Note: The resulting magic square must contain distinct integers in the inclusive range 1 - 9

# Example

# $s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

# The matrix looks like this:

# 5 3 4
# 1 5 8
# 6 4 2

# We can convert it to the following magic square:

# 8 3 4
# 1 5 9
# 6 7 2

# 1 2 3
# 4 5 6
# 7 8 9

# This took three replacements at a cost of

# input: 3 x 3 matrix of integers from 1 - 9
# output: integer, representing the minimum cost to convert the square into a magic square

# obs: magic constant for a 3 x 3 matrix with uniqu integers from 1 - 9 will always be 15


def _getMagicSqaureInfo(s):
    rows = []
    cols = []
    diags = []

    for i in range(len(s)):
        rows.append(sum(s[i]) - 15)

    for j in range(len(s[0])):
        col_sum = 0
        for i in range(len(s)):
            col_sum += s[i][j]
        cols.append(col_sum - 15)

    i = 0
    j = 0
    sum_right_diag = 0

    while i < len(s):
        sum_right_diag += s[i][j]
        i += 1
        j += 1

    diags.append(sum_right_diag - 15)

    i = 0
    j = len(s[0]) - 1
    sum_left_diag = 0

    while i < 3:
        sum_left_diag += s[i][j]
        i += 1
        j -= 1

    diags.append(sum_left_diag - 15)

    return {"rows": rows, "cols": cols, "diags": diags}


def _checkInfo(info, coord, constant):
    row = coord[0]
    col = coord[1]

    row_check = info["rows"][row] - constant
    col_check = info["cols"][col] - constant

    diag_check = []

    if row == col:
        diag_check.append(info["diags"][0] - constant)

    if row + col + 1 == 3:
        diag_check.append(info["diags"][1] - constant)

    return {"row": row_check, "col": col_check, "diag": diag_check}


def _getMissingNums(s):
    numsNeeded = set(range(1, 10))

    for i in range(len(s)):
        for j in range(len(s)):
            numsNeeded.discard(s[i][j])

    return numsNeeded


def formingMagicSquare(s):
    info = _getMagicSqaureInfo(s)
    rows = info["rows"]
    cols = info["cols"]

    diff_matrix = [[0 for _ in range(3)] for _ in range(3)]

    for i in range(len(s)):
        for j in range(len(s)):
            diff_matrix[i][j] = (s[i][j] - rows[i], cols[j])

    return diff_matrix


s = [[4, 5, 8], [2, 4, 1], [1, 9, 7]]

print(formingMagicSquare(s))
