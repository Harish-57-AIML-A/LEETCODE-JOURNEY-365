class Solution:
    def isValidBST(self, root):
        if not root:
            return True
        return (self.isSubtreeLess(root.left, root.val) and
                self.isSubtreeGreater(root.right, root.val) and
                self.isValidBST(root.left) and
                self.isValidBST(root.right))

    def isSubtreeLess(self, node, val):
        if not node: return True
        return node.val < val and self.isSubtreeLess(node.left, val) and self.isSubtreeLess(node.right, val)

    def isSubtreeGreater(self, node, val):
        if not node: return True
        return node.val > val and self.isSubtreeGreater(node.left, val) and self.isSubtreeGreater(node.right, val)
