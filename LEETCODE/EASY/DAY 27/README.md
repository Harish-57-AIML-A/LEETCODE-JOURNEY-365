🌟 Day 27 – Minimum Depth of Binary Tree

📌 **Difficulty**: 🟢 Easy

📌 **Frequency**: 🔥 High

📌 **Link**: [🔗 LeetCode Problem](https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/)

---

## 📝 Problem Statement

Given a binary tree, find its **minimum depth**.

The **minimum depth** is the number of nodes along the **shortest path** from the **root** down to the **nearest leaf node**.

💡 **Note:**

* A **leaf node** is a node with no children.
* Consider **unbalanced trees**, as some branches may be deeper than others.

---

## ❓ Candidate Questions

* **Q:** Can the tree be empty?
  **A:** Yes, return `0`.

* **Q:** What if a node has only one child?
  **A:** Return the minimum depth of the **non-empty subtree**.

* **Q:** Can we optimize for unbalanced trees?
  **A:** Yes, using **BFS** to stop at the first leaf node.

---

## 💡 Approaches

1. **Depth-First Traversal (Recursion)** → `O(n)` time, `O(log n)` space (stack)
2. **Breadth-First Traversal (Level Order)** → `O(n)` time, `O(n)` space (queue)

---

## ☕ Java Solution – Depth-First Traversal (DFS)

```java
public class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        if (root.left == null) return minDepth(root.right) + 1;
        if (root.right == null) return minDepth(root.left) + 1;
        return Math.min(minDepth(root.left), minDepth(root.right)) + 1;
    }
}
```

---

## 🐍 Python Solution – Depth-First Traversal (DFS)

```python
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
```

---

## ☕ Java Solution – Breadth-First Traversal (BFS)

```java
import java.util.*;

public class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        TreeNode rightMost = root;
        int depth = 1;

        while (!q.isEmpty()) {
            TreeNode node = q.poll();

            if (node.left == null && node.right == null) break;

            if (node.left != null) q.add(node.left);
            if (node.right != null) q.add(node.right);

            if (node == rightMost) {
                depth++;
                rightMost = (node.right != null) ? node.right : node.left;
            }
        }

        return depth;
    }
}
```

---

## 🐍 Python Solution – Breadth-First Traversal (BFS)

```python
from collections import deque

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        q = deque([root])
        depth = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
```

---

## 📊 Complexity Analysis

| Approach      | Time ⏱️ | Space 💾         |
| ------------- | ------- | ---------------- |
| DFS Recursion | O(n)    | O(log n) (stack) |
| BFS Iterative | O(n)    | O(n) (queue)     |

---

## ✅ Summary & Key Takeaways

* **DFS Recursive:** Simple, handles missing children carefully.
* **BFS Iterative:** Stops at the **first leaf node**, efficient for **unbalanced trees**.
* **Edge Cases:** Ensure nodes with **single children** are correctly counted.
* **Best Practice:** Use **DFS** for simplicity, **BFS** for performance on highly unbalanced trees.

---
