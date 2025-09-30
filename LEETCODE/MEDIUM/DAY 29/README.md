🌟 Day 29 – Convert Sorted Array to Balanced Binary Search Tree

📌 **Difficulty**: 🟠 Medium

📌 **Frequency**: 🔹 Low

📌 **Link**: [🔗 LeetCode Problem](https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

---

## 📝 Problem Statement

Given a sorted array in **ascending order**, convert it into a **height-balanced Binary Search Tree (BST)**.

A **height-balanced BST** is defined as a tree in which the depth of the two subtrees of every node never differs by more than 1.

**Hint:** This problem is highly **recursive** in nature — think **binary search**.

---

## ❓ Candidate Questions

* **Q:** Which element should I pick as the root?
  **A:** Always pick the **middle element** to maintain balance.

* **Q:** How do we form left and right subtrees?
  **A:** Recursively pick the middle of the left and right subarrays.

* **Q:** Can this approach work with a linked list?
  **A:** Yes, but the implementation changes slightly — see **Day 30**.

---

## 💡 Approach – Divide and Conquer

* Pick the **middle element** of the current subarray → becomes the **root**.
* Recursively build the **left subtree** from the left subarray.
* Recursively build the **right subtree** from the right subarray.
* Repeat until the subarray is empty (`start > end`).

---

## ☕ Java Solution – Divide and Conquer

```java
public class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return sortedArrayToBST(nums, 0, nums.length - 1);
    }

    private TreeNode sortedArrayToBST(int[] arr, int start, int end) {
        if (start > end) return null;
        int mid = (start + end) / 2;
        TreeNode node = new TreeNode(arr[mid]);
        node.left = sortedArrayToBST(arr, start, mid - 1);
        node.right = sortedArrayToBST(arr, mid + 1, end);
        return node;
    }
}
```

---

## 🐍 Python Solution – Divide and Conquer

```python
class Solution:
    def sortedArrayToBST(self, nums):
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node
        
        return build(0, len(nums) - 1)
```

---

## 📊 Complexity Analysis

| Aspect         | Complexity                       |
| -------------- | -------------------------------- |
| Time ⏱️        | O(n) → Each element visited once |
| Space 💾       | O(log n) → Recursion stack depth |
| Methodology 🧩 | Divide & Conquer / Binary Search |

---

## ✅ Summary & Key Takeaways

* Use the **middle element** as root → ensures height-balanced tree.
* Left & right subarrays become **subtrees** recursively.
* Works in **O(n) time** and **O(log n) stack space**.
* Similar to **binary search** — recursively divides the problem.
* Can be adapted for **linked lists** (see Day 30).

---
