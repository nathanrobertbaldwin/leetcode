testCases = int(input())


def majorityOpinion(arr):
    res = set()

    idx = 0
    while idx < len(arr):
        if idx + 1 < len(arr) and arr[idx] == arr[idx + 1]:
            res.add(arr[idx])
        elif idx + 2 < len(arr) and arr[idx] == arr[idx + 2]:
            res.add(arr[idx])

        idx += 1

    if len(res) == 0:
        return -1

    return " ".join(map(str, list(res)))


for test in range(testCases):
    cows = int(input())
    cowsLikeHay = list(map(int, input().split()))
    print(majorityOpinion(cowsLikeHay))
