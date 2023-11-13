function titleToNumber(columnTitle) {
  columnTitle -= 1;
  let map = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  let res = "";

  while (true) {
    if (columnTitle <= 25) return map[columnTitle] + res;
    let remainder = columnTitle % 26;
    res = map[remainder - 1] + res;
    columnTitle = Math.floor(columnTitle / 26);
  }
}

console.log(titleToNumber(27));
