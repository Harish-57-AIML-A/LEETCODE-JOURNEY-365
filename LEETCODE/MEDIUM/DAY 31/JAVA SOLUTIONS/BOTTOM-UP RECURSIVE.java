public TreeNode UpsideDownBinaryTree(TreeNode root) {
    return dfsBottomUp(root, null);
}

private TreeNode dfsBottomUp(TreeNode p, TreeNode parent) {
    if (p == null) return parent;
    TreeNode newRoot = dfsBottomUp(p.left, p);
    p.left = (parent == null) ? null : parent.right;
    p.right = parent;
    return newRoot;
}
