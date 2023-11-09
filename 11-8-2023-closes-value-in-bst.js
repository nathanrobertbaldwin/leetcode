// Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.



// Example 1:


// Input: root = [4,2,5,1,3], target = 3.714286
// Output: 4

function closestValue(root, target) {
    let closest = root.val;
    function searcher(root) {
        if (root.left && target < root.val) searcher(root.left)
        if (Math.abs(root.val - target) <= Math.abs(closest - target)) {
            if (Math.abs(root.val - target === Math.abs(closest - target))) closest = Math.min(root.val, closest);
            else closest = root.val;

        }
        if (root.right && target > root.val) searcher(root.right)
    }
    searcher(root)
    return closest
}

let tree = {
    val: 8,
    left: { val: 1 }
}
console.log(closestValue(tree, 6.0))