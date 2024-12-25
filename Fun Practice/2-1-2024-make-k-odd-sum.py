def make_k_odd_sum(n, k):
    a = list(range(1, n))
    rem = n - 1
    idx = 1

    while rem > k:
        idx += 2

    return a


print(make_k_odd_sum(5, 4))
