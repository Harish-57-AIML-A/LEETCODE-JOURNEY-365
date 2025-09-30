public boolean isValidBST(TreeNode root) {
    if (root == null) return true;
    return isSubtreeLessThan(root.left, root.val)
        && isSubtreeGreaterThan(root.right, root.val)
        && isValidBST(root.left)
        && isValidBST(root.right);
}

private boolean isSubtreeLessThan(TreeNode node, int val) {
    if (node == null) return true;
    return node.val < val 
        && isSubtreeLessThan(node.left, val)
        && isSubtreeLessThan(node.right, val);
}

private boolean isSubtreeGreaterThan(TreeNode node, int val) {
    if (node == null) return true;
    return node.val > val
        && isSubtreeGreaterThan(node.left, val)
        && isSubtreeGreaterThan(node.right, val);
}
