🌟 Day 28 – Balanced Binary Tree

📌 **Difficulty**: 🟢 Easy

📌 **Frequency**: 🔥 High

📌 **Link**: [🔗 LeetCode Problem](https://oj.leetcode.com/problems/balanced-binary-tree/)

---

## 📝 Problem Statement

Given a binary tree, determine if it is **height-balanced**.

A **height-balanced binary tree** is defined as a tree in which **the depth of the two subtrees of every node never differs by more than 1**.

---

## ❓ Candidate Questions

* **Q:** Can the tree be empty?
  **A:** Yes, an empty tree is considered **balanced**.

* **Q:** What is the difference between top-down and bottom-up approaches?
  **A:** Top-down repeatedly calculates depth for each node, whereas bottom-up **passes depth from leaves to root**, avoiding recalculation.

* **Q:** Can we optimize for large trees?
  **A:** Yes, using **bottom-up recursion** for `O(n)` time complexity.

---

## 💡 Approaches

1. **Brute Force Top-Down Recursion** → `O(n²)` time, `O(n)` stack space
2. **Bottom-Up Recursion (Optimized)** → `O(n)` time, `O(n)` stack space

---

## ☕ Java Solution – Brute Force Top-Down

```java
public class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;
        return Math.abs(maxDepth(root.left) - maxDepth(root.right)) <= 1
               && isBalanced(root.left)
               && isBalanced(root.right);
    }

    private int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
```

---

## 🐍 Python Solution – Brute Force Top-Down

```python
class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 and \
               self.isBalanced(root.left) and \
               self.isBalanced(root.right)

    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

---

## ☕ Java Solution – Bottom-Up Recursion (Optimized)

```java
public class Solution {
    public boolean isBalanced(TreeNode root) {
        return maxDepth(root) != -1;
    }

    private int maxDepth(TreeNode root) {
        if (root == null) return 0;
        int L = maxDepth(root.left);
        if (L == -1) return -1;
        int R = maxDepth(root.right);
        if (R == -1) return -1;
        return (Math.abs(L - R) <= 1) ? Math.max(L, R) + 1 : -1;
    }
}
```

---

## 🐍 Python Solution – Bottom-Up Recursion (Optimized)

```python
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
```

---

## 📊 Complexity Analysis

| Approach             | Time ⏱️ | Space 💾     |
| -------------------- | ------- | ------------ |
| Brute Force Top-Down | O(n²)   | O(n) (stack) |
| Bottom-Up Recursion  | O(n)    | O(n) (stack) |

---

## ✅ Summary & Key Takeaways

* **Brute Force:** Simple to implement but **recalculates subtree depths**, costly for degenerated trees → `O(n²)`.
* **Bottom-Up Recursion:** Passes depth from leaves to root, stops early for unbalanced subtree → **O(n) efficiency**.
* **Edge Case Handling:** Ensure leaf nodes and null children are correctly managed.
* 🌟 **Best Practice:** Always prefer **bottom-up recursion** for **balanced tree checks**.

---
