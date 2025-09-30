class Solution:
    def __init__(self):
        self.prev = None

    def isValidBST(self, root):
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if self.prev and root.val <= self.prev.val:
            return False
        self.prev = root
        return self.isValidBST(root.right)
