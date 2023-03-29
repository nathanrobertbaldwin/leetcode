// You are climbing a staircase. It takes n steps to reach the top.

// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

// Example 1:

// Input: n = 2
// Output: 2
// Explanation: There are two ways to climb to the top.
// 1. 1 step + 1 step
// 2. 2 steps
// Example 2:

// Input: n = 3
// Output: 3
// Explanation: There are three ways to climb to the top.
// 1. 1 step + 1 step + 1 step
// 2. 1 step + 2 steps

// function stepCounter(n, path = [], validPaths = []) {
//   if (n < 0) return;
//   if (n === 0) {
//     validPaths.push(path);
//     return;
//   } else {
//     stepCounter(n - 1, [...path, 1], validPaths);
//     stepCounter(n - 2, [...path, 2], validPaths);
//   }
//   return validPaths;
// }

// console.log(stepCounter(6));

// observation - the number of possible paths for n is equal to fib(n)

function stepCounter(n) {
  arr = [1, 2];
  for (let i = 2; i < n; i++) {
    arr[i] = arr[i - 1] + arr[i - 2];
  }
  return arr[n - 1];
}

console.log(stepCounter(6));
