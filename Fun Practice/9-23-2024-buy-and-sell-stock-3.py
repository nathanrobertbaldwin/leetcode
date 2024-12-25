import heapq


def maxProfit(k, prices):

    potential_trades = [0 for _ in prices]

    for day in range(1, len(prices)):
        potential_trades[day] = prices[day] - prices[day - 1]

    # print("before transformation:", potential_trades)

    profit_tracker = 0
    for day in range(1, len(prices)):

        if potential_trades[day] > 0:
            profit_tracker += potential_trades[day]
            potential_trades[day - 1] = 0
            if day == len(prices) - 1:
                potential_trades[day] = profit_tracker

        if potential_trades[day] < 0:
            if profit_tracker > 0:
                potential_trades[day - 1] = profit_tracker
                potential_trades[day] = 0
                profit_tracker = 0

    # print("after transformation:", potential_trades)

    h = []
    for i in range(1, len(potential_trades)):
        if potential_trades[i] > 0:
            heapq.heappush(h, potential_trades[i] * -1)

    sum = 0
    while len(h) > 0 and k > 0:
        sum += heapq.heappop(h) * -1
        k -= 1

    return sum


print(maxProfit(2, prices=[1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))
# should be 13???/


# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

# Example 2:

# Input: k = 2, prices = [3,2,6,5,0,3]
