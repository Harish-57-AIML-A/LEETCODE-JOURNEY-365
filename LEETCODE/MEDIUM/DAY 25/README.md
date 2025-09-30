🌟 Day 25 – Validate Binary Search Tree

📌 **Difficulty**: 🔴 Medium

📌 **Frequency**: 🔥 High

📌 **Link**: [🔗 LeetCode Problem](https://oj.leetcode.com/problems/validate-binary-search-tree/)

---

## 📝 Problem Statement

Given a binary tree, determine if it is a valid **Binary Search Tree (BST)**.

A BST must satisfy:

* The **left subtree** of a node contains only nodes with keys **less than** the node’s key.
* The **right subtree** of a node contains only nodes with keys **greater than** the node’s key.
* Both the left and right subtrees must also be **binary search trees**.

💡 **Note**:
A naive approach that just compares the current node with its immediate children **may fail**, as shown below:

```
    10
   /  \
  5   15
     /  \
    6   20
```

Here, node 6 violates the BST property, even though 10 < 15 and 5 < 10.

---

## ❓ Candidate Questions

* **Q:** Can the tree contain `Integer.MIN_VALUE` or `Integer.MAX_VALUE`?
  **A:** Yes, use `null` as bounds to handle extreme values.

* **Q:** Can we use extra space?
  **A:** Recursive solutions use stack space `O(n)`; iterative in-order traversal can reduce overhead.

* **Q:** Is in-order traversal guaranteed to be sorted for BST?
  **A:** Yes, for a valid BST, in-order traversal produces a strictly increasing sequence.

---

## 💡 Approaches

1. **Brute Force** → `O(n²)` time, `O(n)` space
2. **Top-Down Recursion with Bounds** → `O(n)` time, `O(n)` space
3. **In-Order Traversal** → `O(n)` time, `O(n)` space

---

## ☕ Java Solutions

### 🔹 Brute Force (O(n²))

```java
public boolean isValidBST(TreeNode root) {
    if (root == null) return true;
    return isSubtreeLessThan(root.left, root.val)
        && isSubtreeGreaterThan(root.right, root.val)
        && isValidBST(root.left)
        && isValidBST(root.right);
}

private boolean isSubtreeLessThan(TreeNode node, int val) {
    if (node == null) return true;
    return node.val < val 
        && isSubtreeLessThan(node.left, val)
        && isSubtreeLessThan(node.right, val);
}

private boolean isSubtreeGreaterThan(TreeNode node, int val) {
    if (node == null) return true;
    return node.val > val
        && isSubtreeGreaterThan(node.left, val)
        && isSubtreeGreaterThan(node.right, val);
}
```

---

### 🔹 Top-Down Recursion with Bounds (O(n))

```java
public boolean isValidBST(TreeNode root) {
    return valid(root, null, null);
}

private boolean valid(TreeNode node, Integer low, Integer high) {
    if (node == null) return true;
    if ((low != null && node.val <= low) || (high != null && node.val >= high))
        return false;
    return valid(node.left, low, node.val) && valid(node.right, node.val, high);
}
```

---

### 🔹 In-Order Traversal (O(n))

```java
TreeNode prev = null;

public boolean isValidBST(TreeNode root) {
    if (root == null) return true;
    if (!isValidBST(root.left)) return false;
    if (prev != null && root.val <= prev.val) return false;
    prev = root;
    return isValidBST(root.right);
}
```

---

## 🐍 Python Solutions

### 🔹 Brute Force (O(n²))

```python
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
```

---

### 🔹 Top-Down Recursion with Bounds (O(n))

```python
class Solution:
    def isValidBST(self, root):
        return self.valid(root, None, None)

    def valid(self, node, low, high):
        if not node:
            return True
        if (low is not None and node.val <= low) or (high is not None and node.val >= high):
            return False
        return self.valid(node.left, low, node.val) and self.valid(node.right, node.val, high)
```

---

### 🔹 In-Order Traversal (O(n))

```python
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
```

---

## 📊 Complexity Analysis

| Approach           | Time ⏱️ | Space 💾     |
| ------------------ | ------- | ------------ |
| Brute Force        | O(n²)   | O(n) (stack) |
| Top-Down Recursion | O(n)    | O(n) (stack) |
| In-Order Traversal | O(n)    | O(n) (stack) |

---

## ✅ Summary & Key Takeaways

* **Brute Force:** checks all nodes of subtrees → **O(n²)**, not practical for large trees.
* **Top-Down Recursion:** uses low/high bounds → **O(n)**, clear and safe.
* **In-Order Traversal:** ensures monotonic increasing order → **O(n)**, elegant and simple.
* **Best Methods:** Top-Down or In-Order traversal depending on your style and stack preference.

---
