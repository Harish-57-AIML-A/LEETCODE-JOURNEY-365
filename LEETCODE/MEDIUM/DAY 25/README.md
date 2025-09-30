📘 Day 25 – Validate Binary Search Tree

### 🔗 Problem Link

[Validate Binary Search Tree](https://oj.leetcode.com/problems/validate-binary-search-tree/)
**Difficulty:** Medium
**Frequency:** High

---

## ❓ Question

Given a binary tree, determine if it is a valid Binary Search Tree (BST).

### ✅ BST Properties:

* Left subtree has only nodes with keys **less than** parent’s key.
* Right subtree has only nodes with keys **greater than** parent’s key.
* Both left and right subtrees must also be valid BSTs.

---

## ⚡ Solutions

### 1. Brute Force – Check All Nodes

* For each node, check all values in its left and right subtrees.
* **Time Complexity:** O(n²)
* **Space Complexity:** O(n)

```java
public boolean isValidBST(TreeNode root) {
    if (root == null) return true;
    return isSubtreeLessThan(root.left, root.val)
        && isSubtreeGreaterThan(root.right, root.val)
        && isValidBST(root.left)
        && isValidBST(root.right);
}
private boolean isSubtreeLessThan(TreeNode p, int val) {
    if (p == null) return true;
    return p.val < val
        && isSubtreeLessThan(p.left, val)
        && isSubtreeLessThan(p.right, val);
}
private boolean isSubtreeGreaterThan(TreeNode p, int val) {
    if (p == null) return true;
    return p.val > val
        && isSubtreeGreaterThan(p.left, val)
        && isSubtreeGreaterThan(p.right, val);
}
```

---

### 2. Top-Down Recursion – Pass Bounds

* Carry **low and high limits** down the recursion.
* Quick failure if node breaks BST rules.
* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

```java
public boolean isValidBST(TreeNode root) {
    return valid(root, null, null);
}
private boolean valid(TreeNode p, Integer low, Integer high) {
    if (p == null) return true;
    return (low == null || p.val > low)
        && (high == null || p.val < high)
        && valid(p.left, low, p.val)
        && valid(p.right, p.val, high);
}
```

---

### 3. In-Order Traversal – Monotonic Check

* In-order traversal of BST must be **strictly increasing**.
* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

```java
private TreeNode prev;
public boolean isValidBST(TreeNode root) {
    prev = null;
    return isMonotonicIncreasing(root);
}
private boolean isMonotonicIncreasing(TreeNode p) {
    if (p == null) return true;
    if (isMonotonicIncreasing(p.left)) {
        if (prev != null && p.val <= prev.val) return false;
        prev = p;
        return isMonotonicIncreasing(p.right);
    }
    return false;
}
```

---

# 📊 Overall Complexity Comparison

| Approach           | Time ⏱️ | Space 💾 | Notes                      |
| ------------------ | ------- | -------- | -------------------------- |
| Brute Force        | O(n²)   | O(n)     | Very slow for skewed trees |
| Top-Down Recursion | O(n)    | O(n)     | Elegant, uses bounds       |
| In-Order Traversal | O(n)    | O(n)     | Checks monotonic order     |

---

# 🏁 Summary

✅ Learned **3 ways to validate a BST**: brute force, recursion with bounds, and in-order traversal.
⚡ Optimized solution reduces complexity from **O(n²) → O(n)**.
🌱 Important takeaway: **Pass context (bounds) down recursion** instead of recomputing subtree checks.

---
