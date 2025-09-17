🌟 Day 21 – Add Two Numbers

📌 **Difficulty**: 🟡 Medium
📌 **Frequency**: 🔥 High
📌 **Link**: [🔗 LeetCode Problem](https://leetcode.com/problems/add-two-numbers/)

---

## 📝 Problem Statement

You are given **two linked lists** representing **two non-negative numbers**.

* Digits are stored in **reverse order**.
* Each node contains a single digit.
* Return their sum as a **linked list**.

📌 Example:

```
Input:  (2 → 4 → 3) + (5 → 6 → 4)  
Output: 7 → 0 → 8  
```

---

## ❓ Candidate Clarifications

* **Q:** What if the lists are of different lengths?
  **A:** Continue with the longer list after the shorter one ends.
* **Q:** What if there’s a carry at the end?
  **A:** Add an extra node with value `1`. Example: `(9 → 9) + (1)` → `(0 → 0 → 1)`

---

## 💡 Approach

1. Use a **dummy head** to simplify list creation.
2. Traverse both lists, summing corresponding digits.
3. Maintain a **carry** for sums ≥ 10.
4. Append carry node at the end if needed.

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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode curr = dummyHead;
        int carry = 0;

        while (l1 != null || l2 != null) {
            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;

            int sum = carry + x + y;
            carry = sum / 10;

            curr.next = new ListNode(sum % 10);
            curr = curr.next;

            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        if (carry > 0) {
            curr.next = new ListNode(carry);
        }

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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = carry + x + y
            carry = total // 10
            curr.next = ListNode(total % 10)

            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy.next
```

---

## 📊 Complexity Analysis

| 🔎 Aspect               | ⚡ Optimized Approach                                 |
| ----------------------- | ---------------------------------------------------- |
| ⏱ **Time Complexity**   | `O(max(m, n))` → traverse longer list                |
| 💾 **Space Complexity** | `O(1)` → result stored in linked list itself         |
| 📝 **Notes**            | Handles carry properly, dummy head avoids edge cases |

---

## ✅ Key Takeaways

* Classic **linked list addition problem**.
* Must handle **carry propagation** carefully.
* Dummy head avoids initialization headaches.
* Time efficient: only one pass.

---
