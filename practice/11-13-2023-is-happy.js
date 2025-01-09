function isHappy(n) {
  let sequence = new Set();
  sequence.add(n);

  function nextNum(num) {
    let str = num.toString();
    let ans = 0;

    for (let i = 0; i < str.length; i++) {
      ans += parseInt(str[i]) ** 2;
    }

    if (ans === 1) return true;
    else if (sequence.has(ans)) return false;
    else {
      sequence.add(ans);
      return nextNum(ans);
    }
  }

  return nextNum(n);
}

console.log(isHappy(2));
