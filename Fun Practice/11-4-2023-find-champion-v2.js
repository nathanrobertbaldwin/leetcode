// need path of length n - 1, or there is no champion

// function findChampion(n, edges) {
//   let map = {};

//   for (let i = 0; i < n; i++) {
//     map[i] = [];
//   }

//   edges.forEach(([i, j]) => {
//     map[i].push(j);
//   });

//   let teamPathLengths = {};

//   for (let team in map) {
//     teamPathLengths[team] = 0;
//   }

//   for (let node in map) {
//     let stack = [[node]];
//     while (stack.length) {
//       let currentPath = stack.pop();
//       let currentNode = currentPath[currentPath.length - 1];
//       if (map[currentNode].length === 0) {
//         if (currentPath.length > teamPathLengths[currentPath[0]]) {
//           teamPathLengths[currentPath[0]] = currentPath.length - 1;
//         }
//       } else {
//         map[currentNode].forEach((neighbor) => {
//           let updatedPath = [...currentPath, neighbor.toString()];
//           stack.push(updatedPath);
//         });
//       }
//     }
//   }

//   for (let team in teamPathLengths) {
//     if (teamPathLengths[team] === n - 1) return team;
//   }

//   return -1;
// }

function findChampion(n, edges) {
  let grid = new Array(n).fill(0);

  for (let i = 0; i < grid.length; i++) {
    grid[i] = new Array(n).fill(0);
  }

  edges.forEach(([i, j]) => {
    row = grid[i];
    row[j] = 1;
  });

  let max = 0;
  let winner = -1;
  for (let row = 0; row < grid.length; row++) {
    let sum = 0;
    for (let col = 0; col < grid[0].length; col++) {
      sum += grid[row][col];
    }
    if (sum > max && sum === n - 1) {
      max = sum;
      winner = row;
    }
  }
  return winner;
}

console.log(
  findChampion(3, [
    [0, 2],
    [0, 1],
  ])
);
