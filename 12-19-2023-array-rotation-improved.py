def rowRotation(arr, k):
    k = k % len(arr)
    rotArr = [False] * len(arr)

    arrIdx = len(arr) - 1
    rotArrIdx = k - 1

    while rotArrIdx >= 0:
        rotArr[rotArrIdx] = arr[arrIdx]
        rotArrIdx -= 1
        arrIdx -= 1

    rotArrIdx = k
    arrIdx = 0

    while rotArrIdx < len(rotArr):
        rotArr[rotArrIdx] = arr[arrIdx]
        rotArrIdx += 1
        arrIdx += 1

    return rotArr


print(rowRotation([1, 2, 3, 4, 5], 27))
