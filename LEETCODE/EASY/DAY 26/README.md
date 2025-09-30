🌟 Day 26 – Maximum Depth of Binary Tree

📌 **Difficulty**: 🟢 Easy

📌 **Frequency**: 🔥 High

📌 **Link**: [🔗 LeetCode Problem](https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/)

---

## 📝 Problem Statement

Given a binary tree, find its **maximum depth**.

The **maximum depth** is the number of nodes along the **longest path** from the **root** down to the **farthest leaf node**.

💡 **Note:**

* The maximum depth of an **empty tree** is `0`.
* Each node counts as **1** along the path.

---

## ❓ Candidate Questions

* **Q:** Can the tree be empty?
  **A:** Yes, return `0`.

* **Q:** Should we count the root in the depth?
  **A:** Yes, the root counts as the first level.

* **Q:** Can we solve this iteratively?
  **A:** Yes, using BFS (queue) traversal.

---

## 💡 Approaches

1. **Recursion (DFS)** → `O(n)` time, `O(log n)` space (stack)
2. **Iterative BFS** → `O(n)` time, `O(n)` space (queue)

---

## ☕ Java Solution – Recursive DFS

```java
public class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
```

---

## 🐍 Python Solution – Recursive DFS

```python
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

---

## 📊 Complexity Analysis

| Approach      | Time ⏱️ | Space 💾         |
| ------------- | ------- | ---------------- |
| DFS Recursion | O(n)    | O(log n) (stack) |
| BFS Iterative | O(n)    | O(n) (queue)     |

---

## ✅ Summary & Key Takeaways

* **DFS Recursive:** Simple, elegant, traverses each node once.
* **BFS Iterative:** Level-order traversal, useful for large trees where recursion depth may be a concern.
* **Maximum depth formula:**

```
maxDepth(node) = 1 + max(maxDepth(node.left), maxDepth(node.right))
```

* Best practice: **DFS recursion** is enough for most problems unless tree height is very large.

---
