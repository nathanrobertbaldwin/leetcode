function hasCycle(head) {
  let currNode = head;
  while (currNode.next) {
    if (currNode.next.visited === true) return true;
    else {
      currNode.visited = true;
      currNode = currNode.next;
    }
  }
  return false;
}

// This solution modifies the input, and is also O(n) space complexity.
// Try floyd's algorithm for detecting loops.
// Floyd's algorithm:
// Create two pointers. One that moves at a speed of one node per,
// a second that moves at two nodes per.
// If the second pointer eventually becomes null, then there is no cycle.
// However, if the pointers eventually are equal, there is a cycle.

function detectCycle(head) {
  let slow = head;
  let fast = head;
  while (fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
}

let listZero = { val: 0, next: null };
let listOne = { val: 1, next: null };
let listTwo = { val: 2, next: null };
let listThree = { val: 3, next: null };
let listFour = { val: 4, next: null };
let listFive = { val: 5, next: null };

listZero.next = listOne;
listOne.next = listTwo;
listTwo.next = listThree;
listThree.next = listFour;
listFour.next = listFive;
listFive.next = listThree;

// console.log(detectCycle(listZero));

// Note: It's also possible to detect where the cycle exists.
// After the slow and fast pointers meet, you can create another loop.
// Now, have the slow and fast pointers move at the same speed.
// They will meet at the start point of the cycle.

function detectCycleStart(head) {
  let slow = head;
  let fast = head;
  while (fast.next && fast.next.next) {
    let met = false;
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) {
      met = true;
      slow = head;
    }
    while (met === true) {
      slow = slow.next;
      fast = fast.next;
      if (slow === fast) return slow.val;
    }
  }
  return false;
}

console.log(detectCycleStart(listZero));
