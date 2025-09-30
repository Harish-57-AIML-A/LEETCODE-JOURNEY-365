class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def findMax(node):
            if not node:
                return 0
            left = findMax(node.left)
            right = findMax(node.right)
            
            # Update global maximum path sum
            self.max_sum = max(self.max_sum, node.val + left + right)
            
            # Return max path sum extending to parent
            ret = node.val + max(left, right)
            return max(ret, 0)  # ignore negative sums
        
        findMax(root)
        return self.max_sum
