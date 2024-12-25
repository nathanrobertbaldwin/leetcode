class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
a.next = b;
b.next = c;
// c.next = d;
// d.next = e;
// a -> b -> c

const v = new Node("v");
const w = new Node("w");
const x = new Node("x");
const y = new Node("y");
const z = new Node("z");

v.next = w;
w.next = x;
x.next = y;
y.next = z;

// x -> y -> z

function zipperLists(l1, l2) {
  // Keep track of the head to return later
  let head = l1;

  // Boolean to flip which list we are picking from.
  let pickingFromL1 = true;

  // Temp variables to keep track of the next value to add to the list.
  // We could use l2 instead of this temp variable, but I think this makes it clearer.
  let tempL1 = l1.next;
  let tempL2 = l2;

  // While we have nodes from either list
  while (tempL1 !== null  tempL2 !== null) {
    // If we are working from list one.
    if (pickingFromL1 === true) {
      // If list one still has nodes to pick from.
      if (tempL1 === null) {
        l1.next = tempL2;
        l1 = l1.next;
        tempL2 = tempL2.next;
        continue;
      }

      l1.next = tempL2;
      l1 = l1.next;
      tempL2 = tempL2.next;
    }

    // If we are working from list two.
    if (pickingFromL1 === false) {
      // If list two still has nodes to pick from.
      if (tempL2 === null) {
        l1.next = tempL1;
        l1 = l1.next;
        tempL1 = tempL1.next;
        continue;
      }

      l1.next = tempL1;
      l1 = l1.next;
      tempL1 = tempL1.next;
    }

    // Change which list we are looking at.
    pickingFromL1 = !pickingFromL1;
  }

  return head;
}

console.log(JSON.stringify(zipperLists(a, v)));
// a -> x -> b -> y -> c -> z
