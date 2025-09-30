class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode], parent: Optional[TreeNode] = None) -> Optional[TreeNode]:
        if not root:
            return parent
        newRoot = self.upsideDownBinaryTree(root.left, root)
        root.left = parent.right if parent else None
        root.right = parent
        return newRoot
