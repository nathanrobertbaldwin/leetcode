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

    if tuple_board == (("x", "x", "o"), ("?", "o", "?"), ("?", "?", "?")):
        print()

    if tuple_board in brain:
        return brain[tuple_board]

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
                        outcome = recursion(board, "o", depth + 1)
                    else:
                        outcome = recursion(board, "x", depth + 1)
                    outcomes.append((i, j, outcome[2]))

                board[i][j] = "?"

    best_outcome = outcomes[0]
    if best_outcome[2] != "win":
        # print(outcomes)
        for i, j, outcome in outcomes:
            if best_outcome[2] == "loss":
                if outcome == "win":
                    best_outcome = (i, j, outcome)
                    break
                elif outcome == "draw":
                    best_outcome = (i, j, outcome)
            if best_outcome[2] == "draw":
                if outcome == "win":
                    best_outcome = (i, j, outcome)
                    break

    best_outcome = list(best_outcome)
    if best_outcome[2] == "win":
        best_outcome[2] = "loss"
    elif best_outcome[2] == "loss":
        best_outcome[2] = "win"

    brain[tuple_board] = best_outcome
    return tuple(best_outcome)  # a.k.a brain[board]


"""
789
456
123



"""


def ai_makes_a_move(board, player):
    i, j, outcome_not_used = brain[tuple(tuple(row) for row in board)]
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
who_controls["o"] = ai_makes_a_move

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
