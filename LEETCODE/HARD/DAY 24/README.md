🌟 Day 24 – Copy List with Random Pointer

📌 **Difficulty**: 🔴 Hard

📌 **Frequency**: 🔥 High

📌 **Link**: [🔗 LeetCode Problem](https://oj.leetcode.com/problems/copy-list-with-random-pointer/)

---

## 📝 Problem Statement

You are given a linked list where each node contains:

* A **next** pointer → points to the next node.
* A **random** pointer → points to any node (or `null`).

Return a **deep copy** of this list.

---

## ❓ Example Questions Candidate Might Ask

* **Q:** What if the random pointer is `null`?
  **A:** Then the copied node’s random should also be `null`.

* **Q:** Can we modify the original list?
  **A:** Yes, for the `O(1)` space solution we temporarily modify the original list.

* **Q:** Do we need to preserve node order?
  **A:** Yes, the cloned list should maintain the same structure.

---

## 💡 Approaches

1. **Brute Force** → `O(n²)` time, `O(n)` space (inefficient).
2. **Hash Map** → `O(n)` time, `O(n)` space (map original → copy).
3. **Optimal (Modify Original)** → `O(n)` time, `O(1)` extra space.

---

## ☕ Java Solution – Optimal `O(1)` Space

```java
class RandomListNode {
    int label;
    RandomListNode next, random;
    RandomListNode(int x) { this.label = x; }
}

public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) return null;

        // Step 1: Clone each node and insert it next to original
        RandomListNode p = head;
        while (p != null) {
            RandomListNode copy = new RandomListNode(p.label);
            copy.next = p.next;
            p.next = copy;
            p = copy.next;
        }

        // Step 2: Assign random pointers for the copy
        p = head;
        while (p != null) {
            if (p.random != null) {
                p.next.random = p.random.next;
            }
            p = p.next.next;
        }

        // Step 3: Separate original and copied list
        p = head;
        RandomListNode headCopy = head.next;
        while (p != null) {
            RandomListNode copy = p.next;
            p.next = copy.next;
            copy.next = (p.next != null) ? p.next.next : null;
            p = p.next;
        }

        return headCopy;
    }
}
```

---

## 🐍 Python Solution – Optimal `O(1)` Space

```python
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Step 1: Clone each node and insert it next to original
        p = head
        while p:
            copy = Node(p.val)
            copy.next = p.next
            p.next = copy
            p = copy.next

        # Step 2: Assign random pointers for the copy
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        # Step 3: Separate original and copied list
        p = head
        head_copy = head.next
        while p:
            copy = p.next
            p.next = copy.next
            copy.next = p.next.next if p.next else None
            p = p.next

        return head_copy
```

---

## 📊 Complexity Analysis

| 🔎 Aspect               | ⚡ Optimized Approach                            |
| ----------------------- | ----------------------------------------------- |
| ⏱ **Time Complexity**   | `O(n)` → Three passes over the list             |
| 💾 **Space Complexity** | `O(1)` → No extra data structures               |
| 🧩 **Extra Notes**      | Random pointers assigned via interleaving trick |

---

## ✅ Key Takeaways

* Brute force is **too slow** (`O(n²)`).
* Hash Map solution works, but needs `O(n)` extra memory.
* **Optimal Approach**:

  1. Interleave copies in the original list.
  2. Assign random pointers.
  3. Separate lists back.
* Achieves **O(n) time, O(1) space** efficiency.

---
