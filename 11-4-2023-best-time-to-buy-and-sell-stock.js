// You are given an array prices where prices[i] is the price of a given stock on the ith day.

// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

// Example 1:

// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
// Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
// Example 2:

// Input: prices = [7,6,4,3,1]
// Output: 0
// Explanation: In this case, no transactions are done and the max profit = 0.

function maxProfit(prices) {
  let buyDate = 0;
  let sellDate = 1;

  let maxProfit = 0;

  while (sellDate < prices.length) {
    let buyPrice = prices[buyDate];
    let sellPrice = prices[sellDate];

    if (sellPrice - buyPrice > maxProfit) {
      maxProfit = sellPrice - buyPrice;
      sellDate++;
    } else if (sellPrice - buyPrice < 0) {
      buyDate = sellDate;
    } else {
      sellDate++;
    }
  }
  return maxProfit;
}

// console.log(maxProfit([7, 1, 6, 0, 4, 4]));

// This is a two pointer problem.
// We know that our buyDate must come before the sellDate.
// We want to find the max positive price difference between a buyDate and a sellDate.
// Begin by setting two pointers at the zero and first indices.
// If we have a positive profit, we record as max profit and keep checking.
// If we continue checking and find a negative profit, we have found a smaller buy price.
// It's possible we have already encountered the largest possible profit, however, we should continue checking from the lowest buy price.
// There may be a day in the future we find a larger profit.
// So, we move the buyDate forward to the sale date the produced the negative profit.
// Continue checking with this new buy date.

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
