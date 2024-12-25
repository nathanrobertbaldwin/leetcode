import random


# For double checking: recursively explore all groups
# and return minimum difference. O(2^number of elements)
def find_min_difference_tree(group1, group2, min_difference):

    for i in range(len(group1) - 1, -1, -1):
        group2.append(group1.pop(i))
        min_difference = min(
            abs(sum(group1) - sum(group2)),
            find_min_difference_tree(group1, group2, min_difference),
        )
        group1.append(group2.pop())

    return min_difference


# dp strategy: find sums you can make, then
# explore the different sums to find min difference
def find_min_difference_dp(coins):

    dp = [[] for _ in range(sum(coins) + 1)]
    dp[0].append(0)

    max_sum = 0

    for coin in coins:
        for i in range(max_sum, -1, -1):
            if len(dp[i]) != 0:
                dp[i + coin].append(i)

        max_sum += coin

    left = max_sum // 2

    if left + left == max_sum and len(dp[left]) > 1:
        return 0

    right = left + 1

    while left >= 0 and right <= max_sum:
        if len(dp[left]) == 0:
            left -= 1
        elif len(dp[right]) == 0:
            right += 1
        elif left + right > max_sum:
            left -= 1
        elif left + right < max_sum:
            right += 1
        elif left + right == max_sum:
            return right - left


# for test in range(100):
#     coins = []
#     coins_size = random.randint(1, 10)

#     for coin in range(coins_size):
#         coin_value = random.randint(1, 10)
#         coins.append(coin_value)

#     tree_diff = find_min_difference_tree(coins, [], sum(coins))
#     dp_diff = find_min_difference_dp(coins)

#     if tree_diff != dp_diff:
#         print("tree_diff:", tree_diff)
#         print("dp_diff", dp_diff)
#         print(coins)

print(find_min_difference_dp([2, 4, 7, 11]))
