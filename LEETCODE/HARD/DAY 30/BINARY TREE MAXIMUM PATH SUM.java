class Solution {
    private int maxSum;

    public int maxPathSum(TreeNode root) {
        maxSum = Integer.MIN_VALUE;
        findMax(root);
        return maxSum;
    }

    private int findMax(TreeNode node) {
        if (node == null) return 0;

        int left = findMax(node.left);
        int right = findMax(node.right);

        // Update global maximum path sum
        maxSum = Math.max(maxSum, node.val + left + right);

        // Return max path sum extending to parent
        int ret = node.val + Math.max(left, right);
        return Math.max(ret, 0); // ignore negative sums
    }
}
