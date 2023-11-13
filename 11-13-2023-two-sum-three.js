// 170. Two Sum III - Data structure design
// Easy
// Topics
// Companies
// Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

// Implement the TwoSum class:

// TwoSum() Initializes the TwoSum object, with an empty array initially.
// void add(int number) Adds number to the data structure.
// boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.

// Example 1:

// Input
// ["TwoSum", "add", "add", "add", "find", "find"]
// [[], [1], [3], [5], [4], [7]]
// Output
// [null, null, null, null, true, false]

// Explanation
// TwoSum twoSum = new TwoSum();
// twoSum.add(1);   // [] --> [1]
// twoSum.add(3);   // [1] --> [1,3]
// twoSum.add(5);   // [1,3] --> [1,3,5]
// twoSum.find(4);  // 1 + 3 = 4, return true
// twoSum.find(7);  // No two integers sum up to 7, return false

// Because sets don't contain duplicates, this won't tell me if I'm dealing
// with distinct integers.

class TwoSum {
  constructor() {
    this.values = [];
    this.tracker = {};
  }

  add(num) {
    this.values.push(num);
    if (!(num in this.tracker)) {
      this.tracker[num] = 1;
    } else {
      this.tracker[num]++;
    }
  }

  find(value) {
    for (let i = 0; i < this.values.length; i++) {
      let comp = value - this.values[i];
      if (comp in this.tracker) {
        if (comp !== this.values[i]) return true;
        else {
          if (this.tracker[comp] > 1) return true;
        }
      }
    }
    return false;
  }
}

let test = new TwoSum();

test.add(3);
test.add(2);
test.add(1);

console.log(test.find(2));
console.log(test.find(3));
console.log(test.find(4));
console.log(test.find(5));
console.log(test.find(6));
