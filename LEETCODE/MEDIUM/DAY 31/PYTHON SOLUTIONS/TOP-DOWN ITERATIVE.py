class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        p, parent, parentRight = root, None, None
        
        while p:
            left = p.left
            p.left = parentRight
            parentRight = p.right
            p.right = parent
            parent = p
            p = left
        
        return parent
