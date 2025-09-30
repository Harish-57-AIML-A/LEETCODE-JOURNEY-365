🌟 Day 32 – Binary Tree Upside Down

📌 **Difficulty**: 🟠 Medium

📌 **Frequency**: Medium

📌 **Link**: Coming Soon

---

## 📝 Problem Statement

Given a binary tree where all the **right nodes** are either **leaf nodes with a left sibling** or empty, **flip it upside down** and turn it into a tree where the original right nodes become **left leaf nodes**. Return the new root.

*Example Transformation:*

```
Original Tree:           Flipped Tree:

      1                      4
     / \                    / \
    2   3                  5   2
   / \                        / \
  4   5                      3   1
```

---

## 💡 Approach

At each node, the reassignment follows:

```
p.left  = parent.right
p.right = parent
```

### 1️⃣ Top-Down Iterative Approach

* Keep track of current node `p`, parent node, and parent's right child.
* Update pointers while traversing leftmost path.

```java
public TreeNode UpsideDownBinaryTree(TreeNode root) {
    TreeNode p = root, parent = null, parentRight = null;

    while (p != null) {
        TreeNode left = p.left;
        p.left = parentRight;
        parentRight = p.right;
        p.right = parent;
        parent = p;
        p = left;
    }

    return parent;
}
```

*Observation:* Similar to **reversing a linked list**.

---

### 2️⃣ Bottom-Up Recursive Approach

* Start from **left-most leaf node** (future root).
* Reassign children **bottom-up**, avoiding overwriting issues.

```java
public TreeNode UpsideDownBinaryTree(TreeNode root) {
    return dfsBottomUp(root, null);
}

private TreeNode dfsBottomUp(TreeNode p, TreeNode parent) {
    if (p == null) return parent;
    TreeNode root = dfsBottomUp(p.left, p);
    p.left = (parent == null) ? null : parent.right;
    p.right = parent;
    return root;
}
```

*Observation:* Recursive approach is **cleaner and safer**, especially for deep trees.

---

## 📊 Complexity Analysis

| Approach            | Time ⏱️ | Space 💾 |
| ------------------- | ------- | -------- |
| Top-Down Iterative  | O(n)    | O(1)     |
| Bottom-Up Recursive | O(n)    | O(h)     |

> `h` = height of the binary tree (recursion stack)

---

## ✅ Key Takeaways

* Flip tree **bottom-up** or **top-down** using careful pointer reassignment.
* The **left-most node becomes the new root**.
* Top-down is **iterative and constant space**, but recursive is **easier to reason about**.
* The problem is **similar to reversing a linked list**, but in a tree structure.

---
