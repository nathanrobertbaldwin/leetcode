def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:4]))
    print(sum(arr[1:]))


print(miniMaxSum([1, 4, 2, 5, 3]))
