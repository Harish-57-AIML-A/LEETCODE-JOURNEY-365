🌟 Day 23 – Merge K Sorted Linked Lists

📌 **Difficulty**: 🔴 Hard

📌 **Frequency**: 🔥 High

📌 **Link**: [🔗 LeetCode Problem](https://oj.leetcode.com/problems/merge-k-sorted-lists/)

---

## 📝 Problem Statement

You are given `k` sorted linked lists. Merge them into one sorted linked list and return it.

---

## ❓ Example Questions Candidate Might Ask

* **Q:** Can I merge lists one by one?
  **A:** Yes, but that leads to higher time complexity (`O(nk²)`).

* **Q:** What’s the best approach?
  **A:** Either **Min-Heap (Priority Queue)** or **Divide & Conquer** → both give `O(nk log k)` runtime.

* **Q:** Do we need extra space?
  **A:** Heap method requires `O(k)` extra, divide-and-conquer uses `O(1)`.

---

## 💡 Approaches

1. **Brute Force (One by One Merge)** – `O(nk²)`
2. **Heap / Priority Queue** – `O(nk log k)`
3. **Divide and Conquer** – `O(nk log k)`

---

## ☕ Java Solution – Min Heap Approach

```java
import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class MergeKLists {
    public ListNode mergeKLists(List<ListNode> lists) {
        if (lists == null || lists.isEmpty()) return null;

        Queue<ListNode> heap = new PriorityQueue<>(lists.size(), (a, b) -> a.val - b.val);

        for (ListNode node : lists) {
            if (node != null) heap.add(node);
        }

        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        while (!heap.isEmpty()) {
            ListNode node = heap.poll();
            curr.next = node;
            curr = curr.next;

            if (node.next != null) {
                heap.add(node.next);
            }
        }
        return dummy.next;
    }
}
```

---

## 🐍 Python Solution – Divide & Conquer

```python
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # Divide and Conquer
        def mergeTwoLists(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next, l1 = l1, l1.next
                else:
                    curr.next, l2 = l2, l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(mergeTwoLists(l1, l2))
            lists = merged

        return lists[0]
```

---

## 📊 Complexity Analysis

| Approach             | Time Complexity | Space Complexity |
| -------------------- | --------------- | ---------------- |
| **Brute Force**      | `O(nk²)`        | `O(1)`           |
| **Min Heap**         | `O(nk log k)`   | `O(k)`           |
| **Divide & Conquer** | `O(nk log k)`   | `O(1)` (extra)   |

✅ **Best Choice** → **Heap** or **Divide & Conquer** for efficiency.

---

## ✅ Key Takeaways

* **Dummy head** simplifies list handling.
* **Brute force** is too slow for large `k`.
* **Heap approach** → easy to implement, efficient.
* **Divide & Conquer** → elegant, uses merge sort principle.

---
