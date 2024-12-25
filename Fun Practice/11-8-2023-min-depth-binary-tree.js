// 111. Minimum Depth of Binary Tree
// Easy
// Topics
// Companies
// Given a binary tree, find its minimum depth.

// The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

// Note: A leaf is a node with no children.



// Example 1:


// Input: root = [3,9,20,null,null,15,7]
// Output: 2

function minDepth(root) {
    if (root.left === null && root.right === null) return 1;
    if (root.left !== null && root.right !== null) return Math.min(1 + minDepth(root.left), 1 + minDepth(root.right))
    if (root.left !== null && root.right === null) return 1 + minDepth(root.left)
    if (root.left === null && root.right !== null) return 1 + minDepth(root.right)
}

let tree = {
    val: 2,
    left: null,
    right: {
        val: 3,
        left: null,
        right: {
            val: 4,
            left: null,
            right: {
                val: 5,
                left: null,
                right: {
                    val: 6,
                    left: null,
                    right: null
                }
            }
        }
    }
}



console.log(minDepth(tree))