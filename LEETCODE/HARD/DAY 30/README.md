🌟 Day 31 – Binary Tree Maximum Path Sum

📌 **Difficulty**: 🔴 Hard

📌 **Frequency**: 🔹 Medium

📌 **Link**: [🔗 LeetCode Problem](https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/)

---

## 📝 Problem Statement

Given a **binary tree**, find the **maximum path sum**.

* A path **may start and end at any node** in the tree.
* Example tree:

```
      1
     / \
    2   4
   / \
  2   3
```

* Maximum path sum = **10** (path: 2 → 2 → 3 → 3).

---

## ❓ Candidate Questions

* **Q:** What if the tree is empty?
  **A:** Assume the tree is non-empty.

* **Q:** What if the tree has only a single node?
  **A:** Then the maximum path sum starts and ends at that node.

* **Q:** What if all node values are negative?
  **A:** Return the single node value that is **least negative**.

* **Q:** Does the maximum path need to go through the root?
  **A:** Not necessarily — it can be anywhere in the tree.

---

## 💡 Approach – Bottom-Up DFS

At each node, compute the **maximum path sum** that **passes through this node**:

1. `leftMax = max path sum from left subtree`
2. `rightMax = max path sum from right subtree`
3. `maxSum` at this node = `node.val + leftMax + rightMax`
4. Return to parent: `node.val + max(leftMax, rightMax)`

**Trick:** If a subtree sum is negative, return **0** to ignore it in parent calculation.

---

## ☕ Java Solution – Bottom-Up DFS

```java
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
```

---

## 🐍 Python Solution – Bottom-Up DFS

```python
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
```

---

## 📊 Complexity Analysis

| Aspect         | Complexity                               |
| -------------- | ---------------------------------------- |
| Time ⏱️        | O(n) → Visit each node once              |
| Space 💾       | O(h) → Recursion stack (h = tree height) |
| Methodology 🧩 | Bottom-up DFS, keep track of global max  |

---

## ✅ Key Takeaways

* Bottom-up approach **avoids repeated calculations**.
* Consider **four cases** at each node:

  1. Left subtree + node
  2. Right subtree + node
  3. Left + node + right
  4. Node alone
* Negative path sums are **ignored** to maximize parent path.
* Achieves **O(n) time** and **O(h) space**.

---
