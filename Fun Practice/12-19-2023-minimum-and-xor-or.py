def minAndXorOrPrinter(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print("arr[i]:", arr[i], "bin:", f"{arr[i]:0{4}b}")
            print("arr[j]:", arr[j], "bin:", f"{arr[j]:0{4}b}")
            print("Xor", arr[i] ^ arr[j])
            print("------------------")


print(minAndXorOrPrinter([4, 6, 7]))


# def minAndXorOr(arr):
#     arr.sort()
#     min_diff = arr[1] ^ arr[0]

#     i = 1
#     while i < len(arr) - 1:
#         if arr[i] ^ arr[i + 1] < min_diff:
#             min_diff = arr[i] ^ arr[i + 1]
#         i += 1

#     return min_diff


# print(minAndXorOr([7, 9, 10]))
