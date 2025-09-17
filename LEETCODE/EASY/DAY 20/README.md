🌟 Day 20 – Merge Two Sorted Lists

📌 **Difficulty**: 🟢 Easy

📌 **Frequency**: 🔁 Medium

📌 **Link**: [🔗 LeetCode Problem](https://leetcode.com/problems/merge-two-sorted-lists/)

---

## 📝 Problem Statement

Merge **two sorted linked lists** and return it as a **new sorted list**.
The new list should be made by **splicing together the nodes** of the first two lists.

---

## 💡 Approach

1. Use a **dummy head** node to simplify handling edge cases.
2. Compare nodes of both lists (`l1` and `l2`).
3. Append the smaller node to the merged list.
4. Continue until one list becomes null.
5. Append the remaining nodes of the non-empty list.

---

## ☕ Java Solution

```java
// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode p = dummyHead;

        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                p.next = l1;
                l1 = l1.next;
            } else {
                p.next = l2;
                l2 = l2.next;
            }
            p = p.next;
        }

        if (l1 != null) p.next = l1;
        if (l2 != null) p.next = l2;

        return dummyHead.next;
    }
}
```

---

## 🐍 Python Solution

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2
        return dummy.next
```

---

## 📊 Complexity Analysis

| 🔎 Aspect               | ⚡ Optimized Approach                   |
| ----------------------- | -------------------------------------- |
| ⏱ **Time Complexity**   | `O(m + n)` → traverses both lists once |
| 💾 **Space Complexity** | `O(1)` → only uses dummy pointer       |
| 📝 **Notes**            | In-place merge, no extra list storage  |

---

## ✅ Key Takeaways

* Use of **dummy head** simplifies edge cases.
* Straightforward comparison of two sorted lists.
* Efficient solution with **O(m+n)** time and constant space.

---
