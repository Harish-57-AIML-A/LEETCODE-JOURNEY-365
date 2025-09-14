🚀 Day 18 – Plus One

🔗 **Problem Link:** [LeetCode – Plus One](https://leetcode.com/problems/plus-one/)
📊 **Difficulty:** Easy
🔥 **Frequency:** High

---

## ❓ Problem Statement

You are given a non-negative integer represented as an **array of digits**. Increment the integer by one and return the resulting array.

---

## 💡 Example Questions a Candidate Might Ask

**Q:** Could the number be negative?
**A:** No. Assume it is always **non-negative**.

**Q:** How are the digits ordered? For example, is the number 12 represented by \[1,2] or \[2,1]?
**A:** The digits are stored in **most significant digit first** order → `12 → [1,2]`.

**Q:** Could the number contain leading zeros (like \[0,0,1])?
**A:** No.

---

## 🧠 Approach

1. Start from the **last digit** (least significant).
2. If the digit is **less than 9**, just increment it and return.
3. If the digit is **9**, set it to `0` and move left with a carry.
4. Repeat until no carry remains.
5. Special case: If all digits are 9 (like `[9,9,9]`), result becomes `[1,0,0,0]`.

---

## 🐍 Python Solution

```python
from typing import List

def plusOne(digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
```

---

## ☕ Java Solution

```java
import java.util.*;

public class PlusOne {
    public static List<Integer> plusOne(List<Integer> digits) {
        for (int i = digits.size() - 1; i >= 0; i--) {
            int digit = digits.get(i);
            if (digit < 9) {
                digits.set(i, digit + 1);
                return digits;
            } else {
                digits.set(i, 0);
            }
        }
        digits.add(0); 
        digits.set(0, 1); 
        return digits;
    }
}
```

---

## 📦 Complexity Analysis

| ⏱️ **Time Complexity**                                         | 💾 **Space Complexity**                                          |
| -------------------------------------------------------------- | ---------------------------------------------------------------- |
| **O(n)** – In the worst case (all 9s), we traverse all digits. | **O(1)** – Only modifying input list in place (ignoring output). |

---

## ✅ Example Walkthrough

**Input:** `[9,9,9]`

* Last digit → 9 → becomes 0, carry 1
* Second digit → 9 → becomes 0, carry 1
* First digit → 9 → becomes 0, carry 1
* New digit added at front → `[1,0,0,0]`

**Output:** `[1,0,0,0]`

---
