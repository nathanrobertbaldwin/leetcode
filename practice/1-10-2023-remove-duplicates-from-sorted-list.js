// You are given the heads of two sorted linked lists list1 and list2.

// Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

// Return the head of the merged linked list.

class ListNode {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.length = 0;
  }

  addToHead(val) {
    const newNode = new ListNode(val);

    if (!this.head) {
      this.head = newNode;
    } else {
      newNode.next = this.head;
      this.head = newNode;
    }
    this.length++;
  }
}

function deleteDuplicates(currNode) {
  if (!currNode) return null;

  let newListHead = currNode;
  let freqCounter = {};
  freqCounter[currNode.val] = 1;

  let scanner = currNode.next;

  while (scanner) {
    if (scanner.val in freqCounter) {
      scanner = scanner.next;
    } else {
      freqCounter[scanner.val] = 1;
      currNode.next = scanner;
      currNode = currNode.next;
      scanner = scanner.next;
    }
  }

  currNode.next = scanner;
  return newListHead;
}

function makeList(array) {
  array.reverse();

  const list = new LinkedList();

  array.forEach((element) => {
    list.addToHead(element);
  });

  return list;
}

const listArr = [1, 1, 2, 2, 3, 5];
const list1 = makeList(listArr);
console.log(deleteDuplicates(list1.head));
