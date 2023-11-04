// Given an integer numRows, return the first numRows of Pascal's triangle.

// In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

// Example 1:

// Input: numRows = 5
// Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
// Example 2:

// Input: numRows = 1
// Output: [[1]]

// Nice job checking constraints. 1 <= numRows <= 30

function pascalsTriangle(n) {
  let res = [];
  for (let i = 0; i < n; i++) {
    if (i === 0) res.push([1]);
    else if (i === 1) res.push([1, 1]);
    else {
      let rowI = [];
      rowI.push(1);
      for (let j = 0; j < i - 1; j++) {
        rowI.push(res[i - 1][j] + res[i - 1][j + 1]);
      }
      rowI.push(1);
      res.push(rowI);
    }
  }
  return res;
}

console.log(pascalsTriangle(5));
