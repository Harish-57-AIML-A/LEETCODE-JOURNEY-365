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
  A: The last node remains as it is (not swapped).
* Q: Can I swap by changing **node values** instead of pointers?
  A: No, you must **relink nodes**, not modify values.

---

## 📝 Solution

* Use three pointers:

  * **p** → current node
  * **q** → next node
  * **r** → node after next
* Swap **p and q** by adjusting links:

  ```
  q.next = p  
  p.next = r  
  ```
* Use a **dummy head** to simplify edge cases.
* Continue until no further pairs exist.

---

## 👨‍💻 Java Code

```java
public class SwapNodesInPairs {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode p = head;
        ListNode prev = dummy;

        while (p != null && p.next != null) {
            ListNode q = p.next, r = p.next.next;
            
            prev.next = q;   // connect prev to q
            q.next = p;      // swap
            p.next = r;      // connect p to r
            
            prev = p;        // move prev
            p = r;           // move p
        }
        return dummy.next;
    }
}
```

---

## 📦 Complexity Analysis

| ⏱ Time Complexity             | 💾 Space Complexity                                      |
| ----------------------------- | -------------------------------------------------------- |
| **O(n)** (traverse list once) | **O(1)** (constant space, no recursion/extra structures) |

---
