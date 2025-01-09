# def find_k_odd_sum(n, k):
#     a = list(range(1, n + 1))

#     q = n - 1
#     i = 1
#     dir = -1

#     while i < len(a) - 1 and q > k:
#         if (a[i - 1] + a[i]) % 2 == 1 and (a[i] + a[i + 1]) % 2 == 1:
#             t = a[i]
#             a[i] = a[i + dir]
#             a[i + dir] = t
#             dir = -dir
#             q -= 1

#         i += 1

#     if q > k:
#         t = a[1]
#         a[1] = a[len(a) - 1]
#         a[len(a) - 1] = t

#     count = 0

#     for idx in range(len(a) - 1):
#         if (a[idx] + a[idx + 1]) % 2 == 1:
#             count += 1

#     # return count

#     return " ".join(map(str, a))


# print(find_k_odd_sum(9, 1))


def find_k_odd_sum(n, k):
    res = [1]
    count = 0
    base = 2

    while count < k - 1:
        res.append(base)
        base += 1
        count += 1

    left_base = base + 1
    while left_base <= n:
        res.append(left_base)
        left_base += 2

    while base <= n:
        res.append(base)
        base += 2

    return res


print(find_k_odd_sum(6, 4))
