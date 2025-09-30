class Solution:
    def isBalanced(self, root):
        return self.maxDepth(root) != -1

    def maxDepth(self, root):
        if not root:
            return 0
        L = self.maxDepth(root.left)
        if L == -1:
            return -1
        R = self.maxDepth(root.right)
        if R == -1:
            return -1
        return max(L, R) + 1 if abs(L - R) <= 1 else -1
