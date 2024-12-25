class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const a = new Node(5);
const b = new Node(7);
const c = new Node(10);
const d = new Node(12);
const e = new Node(20);
const f = new Node(28);
a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;
// 5 -> 7 -> 10 -> 12 -> 20 -> 28

const q = new Node(6);
const r = new Node(8);
const s = new Node(9);
const t = new Node(25);
q.next = r;
r.next = s;
s.next = t;
// 6 -> 8 -> 9 -> 25

function mergeSortedLists(L1, L2) {
  let head;
  let tail;

  if (L1.val < L2.val) {
    head = L1;
    tail = L1;
    L1 = L1.next;
  } else {
    head = L2;
    tail = L2;
    L2 = L2.next;
  }

  while (L1 !== null && L2 !== null) {
    if (L1.val < L2.val) {
      tail.next = L1;
      L1 = L1.next;
    } else {
      tail.next = L2;
      L2 = L2.next;
    }
    tail = tail.next;
  }

  if (L1 === null) {
    tail.next = L2;
  }

  if (L2 === null) {
    tail.next = L1;
  }

  return head;
}

console.log(JSON.stringify(mergeSortedLists(a, q)));

// 5 -> 7 -> 10 -> 12 -> 20 -> 28
// 6 -> 8 -> 9 -> 25

// temp1 = 7
// temp2 = 8
// 5 -> 6, l1.next = l2
// 6 -> 7, l2.next = temp1
// l2 = temp2
