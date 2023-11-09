function postorderTraversal(root) {
    let res = []
    if (!root) return res;
    function traverser(root) {
        if (root.left) traverser(root.left)
        if (root.right) traverser(root.right)
        res.push(root.val)
    }
    traverser(root)
    return res;
}