var numberOfPairs = function (points) {
  count = 0;

  for (let i = 0; i < points.length; i++) {
    let x1 = points[i][0];
    let y1 = points[i][1];

    let valid_diags = new Set();
    let sameX = 0;
    let sameY = 0;

    for (let j = 0; j < points.length; j++) {
      if (i === j) continue;

      let x2 = points[j][0];
      let y2 = points[j][1];

      if (sameX === 0 && x1 === x2 && y1 > y2) {
        count++;
        sameX = 1;
      } else if (sameY === 0 && y1 === y2 && x1 < x2) {
        count++;
        sameY = 1;
      } else if (x1 < x2 && y1 > y2) valid_diags.add([x2, y2]);
    }

    let ordered = false;
    while (ordered === false) {
      let badPoint = null;
      for (let diag in valid_diags) {
        x2 = diag[0];
        y2 = diag[1];
        for (let other_diag in valid_diags) {
          let x3 = other_diag[0];
          let y3 = other_diag[1];

          if (x2 === x3 && y2 === y3) continue;
          if (x3 >= x1 && x3 <= x2 && y3 >= y1 && y3 <= y2) {
            badPoint = diag;
          }
        }
      }

      if (badPoint === null) {
        ordered = true;
      } else {
        valid_diags.delete(badPoint);
      }
    }
    count += valid_diags.size;
  }

  return count;
};

let points = [
  [6, 2],
  [4, 4],
  [2, 6],
];

console.log(numberOfPairs(points));
