Day 22 - Swap Nodes in Pairs

🔗 **Problem Link:** [Swap Nodes in Pairs](https://oj.leetcode.com/problems/swap-nodes-in-pairs/)

📊 **Difficulty:** Medium

🔥 **Frequency:** Medium

---

## ❓ Question

Given a linked list, swap every two adjacent nodes and return its head.

**Example:**

```
Input:  1 -> 2 -> 3 -> 4  
Output: 2 -> 1 -> 4 -> 3
```

**Constraints:**

* Only **constant space** allowed.
* You may **not modify values**, only **rearrange nodes**.

---

## 💡 Example Questions Candidate Might Ask

* Q: What if the list has an **odd number of nodes**?
  A: The last node remains unchanged.
* Q: Can I swap by changing **node values** instead of pointers?
  A: No, you must **relink nodes**, not modify values.

---

## 📝 Solution

* Use **dummy head** to simplify edge cases.
* Traverse the list with pointers:

  * **p** → current node
  * **q** → next node
  * **r** → next of next
* Swap links between pairs until list ends.

---

## 👨‍💻 Java Code

```java
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class SwapNodesInPairs {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        while (head != null && head.next != null) {
            ListNode first = head;
            ListNode second = head.next;

            // Swapping
            prev.next = second;
            first.next = second.next;
            second.next = first;

            // Moving pointers forward
            prev = first;
            head = first.next;
        }
        return dummy.next;
    }
}
```

---

## 🐍 Python Code

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first

            # Move pointers
            prev = first
            head = first.next

        return dummy.next
```

---

## 📦 Complexity Analysis

| ⏱ Time Complexity       | 💾 Space Complexity             |
| ----------------------- | ------------------------------- |
| **O(n)** (iterate once) | **O(1)** (constant extra space) |

---
