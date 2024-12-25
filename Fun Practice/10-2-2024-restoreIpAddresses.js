function restoreIpAddresses(s) {
  let res = [];

  // valid length
  if (s.length < 4 || s.length > 12) return res;

  // valid digits
  for (let i = 0; i < s.length; i++) {
    if (s[i] > 5) return res;
  }

  function sumDigits(digits) {
    let sum = 0;
    for (let i = 0; i < digits.length; i++) {
      sum += digits[i];
    }
    return digits;
  }

  function explorer(depth, digits) {
    console.log(digits);
    for (let section = depth; section < 4; section++) {
      for (let num_digits = 1; num_digits <= 3; num_digits++) {
        explorer(depth + 1, [...digits, num_digits]);
      }
    }

    if (depth === 3) {
      if (sumDigits(digits) == s.length) {
        let ip = "";
        let l = 0;
        let section = 0;
        while (section < 4) {
          let new_part = s.slice(l, l + digits[section]) + ".";
          if (new_part[0] == "0") {
            ip = "";
            break;
          }
          l += digits[section];
          section += 1;

          if (ip.length > 0) res.append(ip);
        }
      }
    }
  }

  explorer(0, []);
  return res;
}

let s = "255255111255";
console.log(restoreIpAddresses(s));
