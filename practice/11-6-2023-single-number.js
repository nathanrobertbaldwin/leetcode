// function singleNumber(arr) {
//   let dups = {};
//   arr.forEach((el) => {
//     if (!(el in dups)) dups[el] = 1;
//     else delete dups[el];
//   });
//   return Object.keys(dups)[0];
// }

function singleNumber(nums) {
  let sum = 0;
  for (i = 0; i < nums.length; i++) sum = sum ^ nums[i];
  return sum;
}

console.log(singleNumber([4, 1, 2, 1, 2]));
