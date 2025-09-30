class Solution:
    def isValidBST(self, root):
        return self.valid(root, None, None)

    def valid(self, node, low, high):
        if not node:
            return True
        if (low is not None and node.val <= low) or (high is not None and node.val >= high):
            return False
        return self.valid(node.left, low, node.val) and self.valid(node.right, node.val, high)
