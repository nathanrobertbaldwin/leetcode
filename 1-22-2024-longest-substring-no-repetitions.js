// var lengthOfLongestSubstring = function (s) {
//   const visited = new Set();
//   let longest = 0;
//   let left = 0;

//   for (let right = 0; right < s.length; right++) {
//     const char = s[right];

//     if (visited.has(char)) {
//       while (s[left] !== char) {
//         const previous = s[left];
//         visited.delete(previous);
//         left++;
//       }
//       left++;
//     } else visited.add(char);

//     const len = 1 + right - left;
//     if (len > longest) longest = len;
//   }

//   return longest;
// };

var lengthOfLongestSubstring = function (s) {
  const visited = new Set();
  let longest = 0;
  let left = 0;

  for (let right = 0; right < s.length; right++) {
    const char = s[right];

    if (visited.has(char)) {
      while (s[left] !== char) {
        const previous = s[left];
        visited.delete(previous);
        left++;
      }
      left++;
    } else visited.add(char);

    const len = 1 + right - left;
    if (len > longest) longest = len;
  }

  return longest;
};

let a = "abcasyx";
// 3

let b = "abcbefw";
// 1

console.log(lengthOfLongestSubstring(a));
