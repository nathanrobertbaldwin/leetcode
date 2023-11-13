function majorityElement(nums) {
  let count = {};
  for (let i = 0; i < nums.length; i++) {
    if (!(nums[i] in count)) count[nums[i]] = 1;
    else count[nums[i]]++;
    if (count[nums[i]] > nums.length / 2) return nums[i];
  }
}

console.log(majorityElement([2, 2, 1, 1, 1, 2, 2]));
