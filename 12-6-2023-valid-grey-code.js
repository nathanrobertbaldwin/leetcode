// function grayCode(n) {
//   res = [];
//   function comboMaker(n, height, parent, str) {
//     if (height === n) res.push(str);
//     else {
//       if (parent === 0) {
//         comboMaker(n, height + 1, 1, str + "0");
//       }
//       if (parent === 1) {
//         comboMaker(n, height + 1, 0, str + "1");
//       }
//     }
//   }
//   comboMaker(n, 0, 0, "");
//   return res;
// }

// console.log(grayCode(2));

// function grayCode(n) {
//   res = [];
//   function comboMaker(n, height, bits) {
//     if (height === n - 1) res.push(bits);
//     else {
//       if (bits[height] === bits[height + 1]) {
//         comboMaker(n, height + 1, bits);
//         bits[height] = 1;
//         comboMaker(n, height + 1, bits);
//       } else {
//         bits[height] = 1;
//         comboMaker(n, height + 1, bits);
//         bits[height] = 0;
//         comboMaker(n, height + 1, bits);
//       }
//     }
//   }
//   bits = Array(n).fill(0);
//   comboMaker(n, 0, bits);
//   return res;
// }

// console.log(grayCode(3));

function grayCode(n) {
  let res = [];
  function generator(n, height, str) {
    if (height === n) res.push(str);
    else if (height === 0) {
      generator(n, height + 1, str + "0");
      generator(n, height + 1, str + "1");
    } else {
      firstBit = str[str.length - 1];
      secondBit = str[str.length - 2];
      if (firstBit === secondBit) {
        generator(n, height + 1, str + "0");
        generator(n, height + 1, str + "1");
      } else {
        generator(n, height + 1, str + "1");
        generator(n, height + 1, str + "0");
      }
    }
  }

  let str = "0";
  generator(n, 0, str);
  return res;
}

console.log(grayCode(3));
