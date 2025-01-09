# Input: x = 2, y = 7

# Output: "Alice"

# Explanation:

# The game ends in a single turn:

#     Alice picks 1 coin with a value of 75 and 4 coins with a value of 10.


def losingPlayer(x: int, y: int) -> str:
    aliceLoses = True

    while x >= 1 and y >= 4:
        x -= 1
        y -= 4
        aliceLoses = not aliceLoses

    if aliceLoses:
        return "Bob"
    else:
        return "Alice"


print(losingPlayer(1, 1))
