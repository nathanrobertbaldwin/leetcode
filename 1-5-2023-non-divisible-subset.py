# def _testNonDivisibility(k, subArr):
#     for i in range(len(subArr)):
#         for j in range(i, len(subArr)):
#             if (subArr[i] + subArr[j]) % k == 0:
#                 return False
#     return True


# def nonDivisibleSubset(k, subArr):
#     queue = [subArr]

#     while len(queue) > 0:
#         currSS = queue.pop(0)

#         if _testNonDivisibility(k, currSS) is True:
#             return len(currSS)

#         for i in range(len(currSS)):
#             newSS = currSS[0:i] + currSS[i + 1 :]
#             queue.append(newSS)


# def divByKMaker(k, arr):
#     divByK = {num: 0 for num in arr}

#     for row in range(len(arr)):
#         for col in range(row + 1, len(arr)):
#             if (arr[row] + arr[col]) % k == 0:
#                 divByK[arr[row]] += 1
#                 divByK[arr[col]] += 1

#     return divByK


# def findMinNumCombos(info):
#     min = float("inf")

#     for num in info:
#         if info[num] < min:
#             min = info[num]

#     return min


# def findCountOfMin(info, min):
#     count = 0

#     for num in info:
#         if info[num] == min:
#             count += 1

#     return count


# def removeMaxKDiv(k, arr):
#     info = divByKMaker(k, arr)
#     min = findMinNumCombos(info)
#     countMin = findCountOfMin(info, min)
#     return countMin


# def countCombosNotDiv(k, arr):
#     max_count = 0

#     for row in range(len(arr)):
#         count = 0

#         for col in range(len(arr)):
#             if (arr[row] + arr[col]) % k != 0:
#                 count += 1

#         if count >= max_count:
#             max_count = count

#     return max_count


# def testingRemovalIdea(k, arr):
#     matrix = [[0 for _ in arr] for _ in arr]

#     for row in range(len(arr)):
#         for col in range(len(arr)):
#             if (arr[row] + arr[col]) % k == 0:
#                 matrix[row][col] = 1

#     return matrix


# def _makeRemainderSets(k, arr):
#     rem_set = {}
#     rem_groups = {}

#     for num in arr:
#         rem = num % k
#         if rem in rem_set and rem != 0:
#             rem_set[rem] += 1
#             rem_groups[rem].append(num)
#         else:
#             rem_set[rem] = 1
#             rem_groups[rem] = [num]

#     return (rem_set, rem_groups)


# def nonDivisibleSubset(k, arr):
#     (rem_sets, rem_groups) = _makeRemainderSets(k, arr)
#     return rem_groups
#     rems = list(rem_sets.keys())

#     max_count = 0

#     for i in range(len(rems)):
#         valid_rems = set()
#         valid_rems.add(rems[i])

#         for j in range(len(rems)):
#             if i == j:
#                 continue
#             elif (k - rems[j]) not in valid_rems:
#                 valid_rems.add(rems[j])

#         actual_nums = []
#         count = 0
#         for rem in valid_rems:
#             count += rem_sets[rem]
#             actual_nums = [*actual_nums, *rem_groups[rem]]

#         print(actual_nums)

#         for i in range(len(actual_nums)):
#             for j in range(len(actual_nums)):
#                 if i == j:
#                     continue
#                 print(actual_nums[i], "+", actual_nums[j], "%", k)
#                 print((actual_nums[i] + actual_nums[j]) % k)

#         print("======================")

#         if max_count < count:
#             max_count = count

#     return max_count


# def nonDivisibleSubset(k, arr):
#     rem_arr = [0] * k

#     for num in arr:
#         rem_arr[num % k] += 1

#     return rem_arr


short_nums = [1, 4, 7, 2, 5, 8, 11]

long_nums = [
    61197933,
    56459859,
    319018589,
    271720536,
    358582070,
    849720202,
    481165658,
    675266245,
    541667092,
    615618805,
    129027583,
    755570852,
    437001718,
    86763458,
    791564527,
    163795318,
    981341013,
    516958303,
    592324531,
    611671866,
    157795445,
    718701842,
    773810960,
    72800260,
    281252802,
    404319361,
    757224413,
    682600363,
    606641861,
    986674925,
    176725535,
    256166138,
    827035972,
    124896145,
    37969090,
    136814243,
    274957936,
    980688849,
    293456190,
    141209943,
    346065260,
    550594766,
    132159011,
    491368651,
    3772767,
    131852400,
    633124868,
    148168785,
    339205816,
    705527969,
    551343090,
    824338597,
    241776176,
    286091680,
    919941899,
    728704934,
    37548669,
    513249437,
    888944501,
    239457900,
    977532594,
    140391002,
    260004333,
    911069927,
    586821751,
    113740158,
    370372870,
    97014913,
    28011421,
    489017248,
    492953261,
    73530695,
    27277034,
    570013262,
    81306939,
    519086053,
    993680429,
    599609256,
    639477062,
    677313848,
    950497430,
    672417749,
    266140123,
    601572332,
    273157042,
    777834449,
    123586826,
]

sequential_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

k = 3

custom_nums = [1, 7, 2, 4]


def nonDivisibleSubset(k, s):
    remainderArr = [0] * k
    for i in s:
        remainderArr[i % k] += 1

    maxLength = 0
    maxLength += min(remainderArr[0], 1)

    if k % 2 == 0:
        maxLength += min(remainderArr[k // 2], 1)

    for i in range(1, k // 2 + 1):
        if i != k - i:
            maxLength += max(remainderArr[i], remainderArr[k - i])

    return maxLength


print(nonDivisibleSubset(k, custom_nums))

# can't pick two nums from remainder sets that add to 4
# no two nums from evenly divisible
# no two
