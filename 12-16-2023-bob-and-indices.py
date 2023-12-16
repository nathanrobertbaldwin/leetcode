# Example Input

# Num Test Cases: 2
# Size of first Test Case:3
# A : 0 1 2
# B : 1 0 1
# C: 0 1 2

# Size of Second Test Case: 1
# A: 0
# B: 0
# C: 0


def bobAndIndices(a, b, c):
    aDict = {}

    for i in range(0, len(a)):
        if a[i] in aDict:
            aDict[a[i]] += 1
        else:
            aDict[a[i]] = 1

    findInA = []

    for j in range(0, len(c)):
        findInA.append(b[c[j]])

    count = 0

    for k in range(0, len(findInA)):
        if findInA[k] in aDict:
            count += aDict[findInA[k]]

    return count


a3 = [0, 1, 2]
b3 = [1, 0, 1]
c3 = [0, 1, 2]

a1 = [0]
b1 = [0]
c1 = [0]

print(bobAndIndices(a1, b1, c1))


# testCases = []
# for case in testCases:
#     print(bobAndIndices(case))
