class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

var addTwoNumbers = function (l1, l2) {
  let carry = 0;
  const listHead = new ListNode(0);
  let currNode = listHead;

  while (l1 || l2 || carry) {
    nextVal = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + carry;

    if (nextVal > 9) {
      carry = 1;
      nextVal -= 10;
    } else carry = 0;

    let newNode = new ListNode(nextVal);
    currNode.next = newNode;
    currNode = newNode;

    l1 = l1 ? l1.next : null;
    l2 = l2 ? l2.next : null;
  }

  return listHead.next;
};

function listMaker(arr) {
  let previousNode = new ListNode(arr[0]);
  const listHead = previousNode;
  let nodeIndex = 1;
  while (nodeIndex < arr.length) {
    let newListNode = new ListNode(arr[nodeIndex]);
    previousNode.next = newListNode;
    previousNode = newListNode;
    nodeIndex++;
  }
  return listHead;
}

let L1 = listMaker([2, 4, 3]);
let L2 = listMaker([5, 6, 4]);

console.log(JSON.stringify(addTwoNumbers(L1, L2)));
