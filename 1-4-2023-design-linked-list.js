class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class MyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  get(index) {
    if (index < 0 || index > this.size - 1) return -1;

    let curr = this.head;
    let i = 0;

    while (i < index) {
      curr = curr.next;
      i++;
    }

    return curr.val;
  }

  addAtHead(val) {}

  addAtTail(val) {}

  addAtIndex(index, val) {}

  deleteAtIndex(index) {}
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = new MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */

let first = new Node(1);
let second = new Node(2);
let third = new Node(3);

first.next = second;
second.next = third;

let ourList = new MyLinkedList();
ourList.head = first;
ourList.size = 3;

console.log(ourList.get(2));
