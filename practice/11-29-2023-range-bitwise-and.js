function toBin(num) {
  let arr = new Array(32).fill(0);
  let digit = 31;
  while (num > 0) {
    arr[digit] = num % 2;
    num = Math.floor(num / 2);
    digit--;
  }
  return arr;
}

function rangeBitwiseAnd(left, right) {
  let left_bin = toBin(left);
  let right_bin = toBin(right);
  let res = [];
  let digit = 0;
  while (left_bin[digit] === right_bin[digit]) {
    res[digit] = left_bin[digit];
    digit++;
  }

  while (res.length < 32) {
    res.push(0);
  }

  return parseInt(res.join(""), 2);
}

console.log(rangeBitwiseAnd(5, 7));
