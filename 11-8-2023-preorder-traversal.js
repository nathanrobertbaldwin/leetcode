// Given the root of a binary tree, return the preorder traversal of its nodes' values.



// Example 1:


// Input: root = [1,null,2,3]
// Output: [1,2,3]

function preorderTraversal(root) {
    let res = []
    if (!root) return res;
    function traverser(root) {
        res.push(root.val)
        if (root.left) traverser(root.left)
        if (root.right) traverser(root.right)
    }
    traverser(root)
    return res;
}