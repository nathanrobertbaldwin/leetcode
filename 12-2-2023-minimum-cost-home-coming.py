# def _getValidNeighbors(currPosition, rows, cols):
#     neighbors = []
#     currRow = currPosition[0]
#     currCol = currPosition[1]

#     if currRow > 0:
#         neighbors.append([currRow - 1, currCol])

#     if currRow < rows - 1:
#         neighbors.append([currRow + 1, currCol])

#     if currCol > 0:
#         neighbors.append([currRow, currCol - 1])

#     if currCol < cols - 1:
#         neighbors.append([currRow, currCol + 1])

#     return neighbors


def minCost(startPos, homePos, rowCosts, colCosts):
    initialCost = 0

    rowDir = 1 if startPos[0] < homePos[0] else -1

    for row in range(startPos[0] + rowDir, homePos[0] + rowDir, rowDir):
        initialCost += rowCosts[row]

    colDir = 1 if startPos[1] < homePos[1] else -1

    for col in range(startPos[1] + colDir, homePos[1] + colDir, colDir):
        initialCost += colCosts[col]

    return initialCost


# def minCost(startPos, homePos, rowCosts, colCosts) -> int:
#     pathStart = {"nodes": [startPos], "cost": 0, "set": set()}
#     pathStart["set"].add(tuple(startPos))

#     queue = [pathStart]
#     shortestPathCost = _getInitialCost(startPos, homePos, rowCosts, colCosts)

#     while len(queue) > 0:
#         currPath = queue.pop(0)
#         currPosition = currPath["nodes"][len(currPath["nodes"]) - 1]

#         if currPosition == homePos:
#             shortestPathCost = currPath["cost"]
#             continue

#         neighbors = _getValidNeighbors(currPosition, len(rowCosts), len(colCosts))

#         for neighbor in neighbors:
#             currRow = currPosition[0]
#             currCol = currPosition[1]

#             neighborRow = neighbor[0]
#             neighborCol = neighbor[1]

#             newCost = currPath["cost"]

#             if currRow == neighborRow:
#                 newCost += colCosts[neighborCol]
#             elif currCol == neighborCol:
#                 newCost += rowCosts[neighborRow]

#             if tuple(neighbor) not in currPath["set"] and newCost < shortestPathCost:
#                 newPath = {
#                     "nodes": [*currPath["nodes"], neighbor],
#                     "cost": newCost,
#                     "set": currPath["set"],
#                 }

#                 newPath["set"].add(tuple(neighbor))

#                 queue.append(newPath)

#     return shortestPathCost


startPos = [4, 0]
homePos = [0, 0]
colCosts = [5, 0, 2, 0, 100, 1, 8, 5, 5, 1, 8, 4, 3]
rowCosts = [3, 5, 3, 4, 2, 3, 3, 4, 7, 4, 6, 0, 8]

print(_getInitialCost(startPos, homePos, rowCosts, colCosts))
print(minCost(startPos, homePos, rowCosts, colCosts))
