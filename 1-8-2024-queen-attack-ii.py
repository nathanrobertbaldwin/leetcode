# Function Description

# Complete the queensAttack function in the editor below.

# queensAttack has the following parameters:
# - int n: the number of rows and columns in the board
# - nt k: the number of obstacles on the board
# - int r_q: the row number of the queen's position
# - int c_q: the column number of the queen's position
# - int obstacles[k][2]: each element is an array of
# integers, the row and column of an obstacle


def _convert(size, pre_row, pre_col):
    row = size - pre_row
    col = pre_col - 1
    return (row, col)


def _make_init_queen_bounds(size, queenRow, QueenCol):
    (row, col) = _convert(size, queenRow, QueenCol)

    tl_near_edge = min(row, col)
    tr_near_edge = min(row, size - col - 1)
    br_near_edge = min(size - row - 1, size - col - 1)
    bl_near_edge = min(size - row - 1, col)

    queenInfo = {
        "q": (row, col),
        "t": (0, col),
        "r": (row, size - 1),
        "b": (size - 1, col),
        "l": (row, 0),
        "tl": (row - tl_near_edge, col - tl_near_edge),
        "tr": (row - tr_near_edge, col + tr_near_edge),
        "br": (row + br_near_edge, col + br_near_edge),
        "bl": (row + bl_near_edge, col - bl_near_edge),
    }

    return queenInfo


def _update_queen_bounds(size, queen_bounds, obstacles):
    (queen_row, queen_col) = queen_bounds["q"]

    for obstacle in obstacles:
        pre_row = obstacle[0]
        pre_col = obstacle[1]
        (obstacle_row, obstacle_col) = _convert(size, pre_row, pre_col)

        if obstacle_row == queen_row:
            if obstacle_col > queen_bounds["l"][1] and obstacle_col < queen_col:
                queen_bounds["l"] = (obstacle_row, obstacle_col + 1)
            elif obstacle_col < queen_bounds["r"][1] and obstacle_col > queen_col:
                queen_bounds["r"] = (obstacle_row, obstacle_col - 1)

        if obstacle_col == queen_col:
            if obstacle_row > queen_bounds["t"][0] and obstacle_row < queen_row:
                queen_bounds["t"] = (obstacle_row + 1, obstacle_col)
            elif obstacle_row < queen_bounds["b"][0] and obstacle_row > queen_row:
                queen_bounds["b"] = (obstacle_row - 1, obstacle_col)

        if obstacle_row - queen_row == obstacle_col - queen_col:
            if obstacle_row > queen_bounds["tl"][0] and obstacle_row < queen_row:
                queen_bounds["tl"] = (obstacle_row + 1, obstacle_col + 1)
            elif obstacle_row < queen_bounds["br"][0] and obstacle_row > queen_row:
                queen_bounds["br"] = (obstacle_row - 1, obstacle_col - 1)

        if obstacle_row - queen_row == -(obstacle_col - queen_col):
            if obstacle_row > queen_bounds["tr"][0] and obstacle_row < queen_row:
                queen_bounds["tr"] = (obstacle_row + 1, obstacle_col - 1)
            elif obstacle_row < queen_bounds["bl"][0] and obstacle_row > queen_row:
                queen_bounds["bl"] = (obstacle_row - 1, obstacle_col + 1)

    return queen_bounds


def queensAttack(size, obsCount, queen_pre_row, queen_pre_col, obstacles):
    queen_bounds = _make_init_queen_bounds(size, queen_pre_row, queen_pre_col)
    queen_bounds = _update_queen_bounds(size, queen_bounds, obstacles)

    (queen_row, queen_col) = queen_bounds["q"]
    del queen_bounds["q"]

    count = 0

    for bound in queen_bounds:
        bound_row = queen_bounds[bound][0]
        bound_col = queen_bounds[bound][1]

        if bound in ("tl", "tr", "bl", "br"):
            count += abs(bound_row - queen_row)
        else:
            count += max(abs(bound_row - queen_row), abs(bound_col - queen_col))

    return count


print(queensAttack(4, 0, 4, 4, []))
# 5 5
# 4 2
# 2 3
# Expect: 10
