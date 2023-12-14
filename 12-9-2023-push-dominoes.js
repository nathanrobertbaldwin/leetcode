// function nextLeft(dominoes, RIdx) {
//   for (let LIdx = RIdx; LIdx < dominoes.length; LIdx++) {
//     if (dominoes[LIdx] === "L") {
//       return LIdx;
//     }
//   }
//   return -1;
// }

// function pushDominoes(dominoes) {
//   let res = new Array(dominoes.length).fill("0");
//   let rAndLPairs = {};

//   for (let i = 0; i < dominoes.length; i++) {
//     if (dominoes[i] === "R") {
//       left = nextLeft(dominoes, i);
//       rAndLPairs[left] = i;
//     }
//   }

//   for (key in rAndLPairs) {
//     let LIdx = parseInt(key);
//     let RIdx = rAndLPairs[key];
//     let distance = LIdx - RIdx;
//     if (distance === 2) {
//       res[RIdx] = "R";
//       res[RIdx + 1] = ".";
//       res[LIdx] = "L";
//     }
//   }

//   for (let i = 0; i < res.length - 1; i++) {
//     if (res[i] !== "0") continue;
//     if (dominoes[i + 1] === "L") {
//       res[i] = "L";
//       res[i + 1] = "L";
//     }
//   }

//   for (let i = res.length - 1; i > 0; i--) {
//     if (res[i] !== "0") continue;
//     if (dominoes[i - 1] === "R") {
//       res[i] = "R";
//       res[i - 1] = "R";
//     }
//   }

//   for (let i = 0; i < res.length - 1; i++) {
//     if (res[i] == "0") res[i] == ".";
//   }

//   if (res[0] === "." && dominoes[0] !== ".") res[0] = dominoes[0];
//   if (res[res.length - 1] === "." && dominoes[dominoes.length - 1] !== ".")
//     res[res.length - 1] = dominoes[dominoes.length - 1];

//   return res.join("");
// }

// // Input: dominoes = ".L.R...LR..L.."
// // Output: "LL.RR.LLRRLL.."

// console.log(pushDominoes("RR.L"));

function pushDominoes(dominoes) {
  res = [];

  while (res.length < dominoes.length) {
    res.push({ char: ".", set: false });
  }

  for (let i = 0; i < dominoes.length - 1; i++) {
    if (dominoes.slice(i, i + 2) === "RL") {
      res[i].char = "R";
      res[i + 1].char = "L";
      res[i].set = res[i + 1].set = true;
    } else if (dominoes.slice(i, i + 2) === "LR") {
      res[i].char = "L";
      res[i].set = true;

      res[i + 1].char = "R";
      res[i + 1].set = true;
    }
  }

  for (let i = 0; i < dominoes.length - 2; i++) {
    if (dominoes.slice(i, i + 3) === "R.L") {
      res[i].char = "R";
      res[i].set = true;

      res[i + 1].char = ".";
      res[i + 1].set = true;

      res[i + 2].char = "L";
      res[i + 2].set = true;
    }
  }

  for (let i = 0; i < res.length; i++) {
    if (res[i].set === false) {
      if (dominoes[i - 1] === "R") {
        res[i - 1].char = res[i].char = "R";
        res[i - 1].set = res[i].set = true;
      } else if (dominoes[i + 1] === "L") {
        res[i].char = res[i + 1].char = "L";
        res[i].set = res[i + 1].set = true;
      } else {
        res[i].char = dominoes[i];
        res[i].set = true;
      }
    }
  }

  let str = "";
  res.forEach((o) => (str += o.char));
  return str;
}

// Input: dominoes = ".L.R...LR..L.."
// Output: "LL.RR.LLRRLL.."

console.log(pushDominoes("RL"));
