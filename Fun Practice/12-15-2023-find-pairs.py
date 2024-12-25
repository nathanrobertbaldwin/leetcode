import random


def findPairsBrute(arr):
    pairs = 0

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] - arr[j]) / (i - j) == 1:
                pairs += 2

    return pairs


# def findPairsMask(arr):
#     pairs = 0

#     for i in range(0, len(arr)):
#         if arr[i] == 0:
#             continue
#         left = i
#         right = i + 1
#         pairs_for_arri = 0
#         future_pairs = 0
#         while right < len(arr):
#             if (arr[left] - arr[right]) / (left - right) == 1:
#                 future_pairs += 2
#                 pairs_for_arri += future_pairs
#                 arr[left] = 0
#                 left = right
#                 right += 1
#             elif right == len(arr) - 1:
#                 arr[left] = 0
#                 left = right
#                 right += 1
#             else:
#                 right += 1

#         pairs += pairs_for_arri

#     return pairs


def findPairs(arr):
    dict = {}

    for i in range(0, len(arr)):
        if (arr[i] - i) in dict:
            dict[arr[i] - i] += 1
        else:
            dict[arr[i] - i] = 0

    pairs = 0

    for key in dict:
        if dict[key] > 0:
            pairs += dict[key] * (dict[key] + 1)

    return pairs


arr = [1, 2, 3, 4]

print(findPairsBrute(arr))
print(findPairs(arr))

# n = random.randint(1, 30)
# print(n)
# arr = []
# inputStr = ""

# for i in range(0, n):
#     random_integer = random.randint(1, n)
#     inputStr += str(random_integer) + " "
#     arr.append(random_integer)

# print(inputStr)
