# Ex:
# a = [3, 2, 2]
# b = [1, 3, 1, 3]

# # test

# a = [5, 2]
# a = [3, 4]
# a = [7]

# b = [4, 1, 3]
# b = [1, 4, 3]
# b = [1, 3, 4]


def makeAllSubArrs(arr):
    subArrs = set()
    subArrs.add(tuple(arr))
    
    if len(arr) <= 1:
        return subArrs
    
    def explorer(arr):
        if len(arr) == 2:
            subArrs.add(tuple([arr[0] + arr[1]]))
        else:
            i = 0

            while i + 1 < len(arr):
                newSubArr = [*arr[0:i], arr[i] + arr[i + 1], *arr[i + 2 : len(arr)]]
                if tuple(newSubArr) not in subArrs:
                    subArrs.add(tuple(newSubArr))
                    explorer(newSubArr)
                i += 1

    explorer(arr)
    return subArrs


def equalSubArrs(arrA, arrB):
    subArrsA = makeAllSubArrs(arrA)
    subArrsB = makeAllSubArrs(arrB)

    longest = -1

    for subArr in subArrsA:
        if subArr in subArrsB:
            if len(subArr) > longest:
                longest = len(subArr)

    return longest


arrA = [1, 3, 2, 2, 3]
arrB = [4, 2, 5]

print(equalSubArrs(arrA, arrB))
