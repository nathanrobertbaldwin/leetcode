def makeSupersetsDFS(a, currSS=[], depth=0, superS=[]):
    if depth == len(a):
        superS.append(currSS)
    else:
        makeSupersetsDFS(a, [*currSS], depth + 1, superS)
        makeSupersetsDFS(a, [a[len(a) - depth - 1], *currSS], depth + 1, superS)

    return superS


a = [1, 2, 3, 4, 5]

# print(makeSupersetsDFS(a))


def makeSuperSetsBFS(a):
    superS = set()
    queue = [a]

    while len(queue) > 0:
        currSS = queue.pop(0)
        for i in range(len(currSS)):
            newSS = currSS[0:i] + currSS[i + 1 :]
            queue.append(newSS)
            superS.add(tuple(newSS))

    return superS


print(makeSuperSetsBFS(a))
