def organizingContainers(container):
    ball_counter = {j: 0 for j in range(len(container))}
    total_ball_counter = {}

    i = 0
    j = 0

    while i < len(container):
        total_balls = 0

        while j < len(container[i]):
            ball_counter[j] += container[i][j]
            total_balls += container[i][j]
            j += 1

        if total_balls in total_ball_counter:
            total_ball_counter[total_balls] += 1
        else:
            total_ball_counter[total_balls] = 1

        total_balls = 0
        j = 0
        i += 1

    for ball in ball_counter:
        if (
            ball_counter[ball] in total_ball_counter
            and total_ball_counter[ball_counter[ball]] > 0
        ):
            total_ball_counter[ball_counter[ball]] -= 1
        else:
            return "Impossible"

    return "Possible"


print(organizingContainers([[1, 1], [1, 1]]))
print(organizingContainers([[0, 2], [1, 1]]))
