import random


def findPairsBrute(arr):
    pairs = 0

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] - arr[j]) / (i - j) == 1:
                pairs += 2

    return pairs


def findPairsMask(arr):
    pairs = 0

    for i in range(0, len(arr)):
        if arr[i] == 0:
            continue
        left = i
        right = i + 1
        pairs_for_arri = 0
        future_pairs = 0
        while right < len(arr):
            if (arr[left] - arr[right]) / (left - right) == 1:
                future_pairs += 2
                pairs_for_arri += future_pairs
                arr[left] = 0
                left = right
                right += 1
            elif right == len(arr) - 1:
                arr[left] = 0
                left = right
                right += 1
            else:
                right += 1

        pairs += pairs_for_arri

    return pairs


def findPairsDict(arr):
    dict = {}
    for i in range(0, len(arr)):
        if arr[i] < len(arr):
            print(arr[i], arr[arr[i]])

    return dict


arr = [11, 10, 8, 10, 1, 6, 1, 9, 8, 7, 2, 6, 4]
print(findPairsDict(arr))

# n = random.randint(1, 30)
# print(n)
# arr = []
# inputStr = ""

# for i in range(0, n):
#     random_integer = random.randint(1, n)
#     inputStr += str(random_integer) + " "
#     arr.append(random_integer)

# print(inputStr)
print(findPairsBrute(arr))
print(findPairsMask(arr))
