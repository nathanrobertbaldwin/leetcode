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

# def _checkInfo(info, coord, constant):
#     row = coord[0]
#     col = coord[1]

#     row_check = info[rows][row] - constant
#     col_check = info[cols][col] - constant

#     diag_check = []

#     if row == col:
#         diag_check.append(info[diags][0] - constant)

#     if row + col + 1 == 3:
#         diag_check.append(info[diags][1] - constant)

#     return {row: row_check, col: col_check, diag: diag_check}


# def _getMissingNums(s):
#     numsNeeded = set(range(1, 10))

#     for i in range(len(s)):
#         for j in range(len(s)):
#             numsNeeded.discard(s[i][j])

#     return numsNeeded


# def _canAddNumToSquare(square, num):
#     for row in range(len(square)):
#         for col in range(len(square)):
#             if square[row][col] == num:
#                 return False

#     return True


# def _hasValidRows(square):
#     for row in square:
#         if 0 not in row:
#             if sum(row) != 15:
#                 return False
#     return True


# def testingMagicCombos():
#     squares = set()

#     def squareMaker(square, row=0, col=0):
#         for row in range(len(square)):
#             for col in range(len(square)):
#                 if square[row][col] == 0:
#                     for num in range(1, 10):
#                         if _canAddNumToSquare(square, num) == True:
#                             square[row][col] = num
#                             if _hasValidRows(square):
#                                 squareMaker(square, row, col)
#                         if num == 9:
#                             return

#                         square[row][col] = 0

#         if (_checkValidSquare(square)) == True:
#             squares.add(str(square))
#             print(squares)

#     start_square = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#     squareMaker(start_square)
#     return squares


# print(testingMagicCombos())


# def _checkMagicConstant(s):
#     rows = []
#     cols = []
#     diags = []

#     for i in range(len(s)):
#         rows.append(sum(s[i]))

#     for j in range(len(s[0])):
#         col_sum = 0
#         for i in range(len(s)):
#             col_sum += s[i][j]
#         cols.append(col_sum)

#     i = 0
#     j = 0
#     sum_right_diag = 0

#     while i < len(s):
#         sum_right_diag += s[i][j]
#         i += 1
#         j += 1

#     diags.append(sum_right_diag)

#     i = 0
#     j = len(s[0]) - 1
#     sum_left_diag = 0

#     while i < 3:
#         sum_left_diag += s[i][j]
#         i += 1
#         j -= 1

#     diags.append(sum_left_diag)

#     square_sums = [*rows, *cols, sum_right_diag, sum_left_diag]

#     for num in square_sums:
#         if num != 15:
#             return False

#     return True


# def _hasNoDuplicates(square):
#     has_nums = set()
#     for i in range(len(square)):
#         for j in range(len(square)):
#             if square[i][j] in has_nums:
#                 return False
#             else:
#                 has_nums.add(square[i][j])
#     return True


# def makeCombosOfFifteen():
#     fifteens = set()
#     for i in range(1, 10):
#         for j in range(1, 10):
#             for k in range(1, 10):
#                 if i + j + k == 15:
#                     if (i, j, k) not in fifteens:
#                         fifteens.add((i, j, k))
#     return fifteens


# combos = makeCombosOfFifteen()


# def makeMagicSquares(combos):
#     magic_squares = set()
#     for combo_one in combos:
#         for combo_two in combos:
#             for combo_three in combos:
#                 row1 = list(combo_one)
#                 row2 = list(combo_two)
#                 row3 = list(combo_three)
#                 new_square = [row1, row2, row3]
#                 if _checkMagicConstant(new_square) and _hasNoDuplicates(new_square):
#                     magic_squares.add(str(new_square))
#     return magic_squares


def formingMagicSquares(square):
    valid_squares = [
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    ]

    min_cost = float("inf")

    for valid_square in valid_squares:
        curr_cost = 0
        for row in range(len(square)):
            for col in range(len(square)):
                curr_cost += abs(valid_square[row][col] - square[row][col])
        if curr_cost < min_cost:
            min_cost = curr_cost

    return min_cost


# Sample inputs
s1 = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

s2 = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]

s3 = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]

print(formingMagicSquares(s3))
