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

function pascalsTriangleRowN(n) {
  let triangle = pascalsTriangle(n + 1);
  return triangle[n];
}

console.log(pascalsTriangleRowN(6));
