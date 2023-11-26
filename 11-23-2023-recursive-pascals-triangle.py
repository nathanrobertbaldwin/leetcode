def getRow(rowIndex: int):
    zero = [[1]]

    if rowIndex == 0:
        return zero

    def triangleMaker(rowIndex, currHeight, currTriangle):
        if currHeight > rowIndex:
            return currTriangle[currHeight - 1]
        else:
            newRow = []

            for i in range(0, currHeight + 1):
                if i == 0 or i == currHeight:
                    newRow.append(1)
                else:
                    newRow.append(
                        currTriangle[currHeight - 1][i - 1]
                        + currTriangle[currHeight - 1][i]
                    )

            currTriangle.append(newRow)

            return triangleMaker(rowIndex, currHeight + 1, currTriangle)

    return triangleMaker(rowIndex, 1, zero)


print(getRow(5))
