def findErrorNums(arr):
    res = [0] * 2

    need_nums = set(range(1, len(arr) + 1))

    for num in arr:
        if num in need_nums:
            need_nums.discard(num)
        else:
            res[0] = num

    res[1] = need_nums.pop()
    return res


print(findErrorNums([1, 2, 2, 4]))
