brain = {}


def weHaveAWinner(board):
    # 3 in a row
    for k in range(len(board)):
        if board[k][0] != "?":
            if board[k][1] == board[k][0] and board[k][2] == board[k][0]:
                return True
        # 3 in a col
        if board[0][k] != "?":
            if board[1][k] == board[0][k] and board[2][k] == board[0][k]:
                return True

    if board[1][1] != "?":
        # first diagonal
        if board[0][0] == board[1][1] and board[2][2] == board[0][0]:
            return True

        # second  diagonal
        if board[0][2] == board[1][1] and board[2][0] == board[1][1]:
            return True

    return False


def recursion(board, player, depth):

    tuple_board = tuple(tuple(row) for row in board)

    # if tuple_board == (('x', 'x', 'o'), ('?', 'o', '?'), ('?', '?', '?')):
    #     print()

    if tuple_board in brain:
        return brain[tuple_board][0][2]

    outcomes = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "?":
                board[i][j] = player

                if weHaveAWinner(board):
                    outcomes.append((i, j, "win"))

                elif depth == 9:
                    outcomes.append((i, j, "draw"))
                    board[i][j] = "?"
                    break  # no other empty cells to search for

                else:
                    if (
                        player == "x"
                    ):  # think of the opposite, if opponent tells me its win for him, then its loss for me
                        result = recursion(board, "o", depth + 1)
                    else:
                        result = recursion(board, "x", depth + 1)

                    outcomes.append((i, j, result))
                board[i][j] = "?"

    best_result = outcomes[0][2]
    if best_result != "win":
        # print(outcomes)
        for i, j, outcome in outcomes:
            if best_result == "loss":
                if outcome == "win":
                    best_result = outcome
                    break
                elif outcome == "draw":
                    best_result = outcome
            if best_result == "draw":
                if outcome == "win":
                    best_result = outcome
                    break

    best_outcomes = []
    for i, j, result in outcomes:
        if result == best_result:
            best_outcomes.append((i, j, result))  # i,j

    brain[tuple_board] = best_outcomes  # list of tuples

    if best_result == "win":
        best_result = "loss"
    elif best_result == "loss":
        best_result = "win"

    return best_result


"""
789
456
123



"""

from random import randint


def ai_makes_a_move(board, player):
    best_moves = brain[tuple(tuple(row) for row in board)]
    i, j, _ = best_moves[randint(0, len(best_moves) - 1)]
    # print(tuple(tuple(row) for row in board))
    board[i][j] = player


def human_makes_a_move(board, player):
    i = None
    j = None

    # print(tuple(tuple(row) for row in board))

    while True:
        n = int(input())
        if n == 7:
            i, j = 0, 0
        elif n == 8:
            i, j = 0, 1
        elif n == 9:
            i, j = 0, 2
        elif n == 4:
            i, j = 1, 0
        elif n == 5:
            i, j = 1, 1
        elif n == 6:
            i, j = 1, 2
        elif n == 1:
            i, j = 2, 0
        elif n == 2:
            i, j = 2, 1
        elif n == 3:
            i, j = 2, 2
        else:
            print("incorrect number, input again")
            continue
        if board[i][j] != "?":
            print("cell occupied, input again")
            continue

        board[i][j] = player
        break


board = [["?" for i in range(3)] for j in range(3)]

recursion(board, player="x", depth=1)

who_controls = {}
who_controls["x"] = ai_makes_a_move
who_controls["o"] = human_makes_a_move
# for key, value in brain.items():
#     print(key,value)
print(len(brain.keys()))


player = "x"
for number_of_moves in range(9):
    print()
    # for i in board:
    #     print(*i )
    fn = who_controls[player]
    fn(board, player)
    outcome = weHaveAWinner(board)

    print()

    for i in board:
        print(*i)
    if outcome == True:
        print(player, "won")
        break
    elif number_of_moves == 8:
        print("draw")
        break

    if player == "x":
        player = "o"
    else:
        player = "x"
