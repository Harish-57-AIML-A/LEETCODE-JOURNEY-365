🌟 Day 18 – Plus One

📌 **Difficulty**: 🟢 Easy

📌 **Frequency**: 🔥 High

📌 **Link**: [🔗 LeetCode Problem](https://leetcode.com/problems/plus-one/)

---

## 📝 Problem Statement

You are given a **non-negative integer** represented as an array of digits. Add **one** to this number and return the new array.

Examples:

* `[1,2,3]` → `[1,2,4]`
* `[4,3,2,1]` → `[4,3,2,2]`
* `[9,9,9]` → `[1,0,0,0]`

⚠️ Digits are stored with the **most significant digit first**.

---

## ❓ Example Questions Candidate Might Ask

* **Q:** Could the number be negative?
  **A:** No, assume it’s always **non-negative**.

* **Q:** Could it contain leading zeros?
  **A:** No.

* **Q:** How are digits stored?
  **A:** **Most significant digit at the head** → `12 = [1,2]`.

---

## 💡 Approach

1. Start from the **last digit** (least significant).
2. If digit < 9 → increment and return.
3. If digit == 9 → set to 0 and carry over.
4. If all digits are 9 → prepend `1` (e.g., `[9,9,9] → [1,0,0,0]`).

---

## ☕ Java Solution

```java
import java.util.*;

public class PlusOne {
    public List<Integer> plusOne(List<Integer> digits) {
        for (int i = digits.size() - 1; i >= 0; i--) {
            int digit = digits.get(i);

            if (digit < 9) {
                digits.set(i, digit + 1);
                return digits;
            } else {
                digits.set(i, 0);
            }
        }

        // If all digits were 9
        digits.add(0);  
        digits.set(0, 1);
        return digits;
    }

    public static void main(String[] args) {
        PlusOne sol = new PlusOne();
        System.out.println(sol.plusOne(new ArrayList<>(Arrays.asList(1,2,3)))); // [1,2,4]
        System.out.println(sol.plusOne(new ArrayList<>(Arrays.asList(9,9,9)))); // [1,0,0,0]
    }
}
```

---

## 🐍 Python Solution

```python
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If all were 9s
        return [1] + digits


# 🚀 Example Run
sol = Solution()
print(sol.plusOne([1,2,3]))   # [1,2,4]
print(sol.plusOne([9,9,9]))   # [1,0,0,0]
```

---

## 📊 Complexity Analysis

| 🔎 Aspect                 | ⚡ Optimized Approach                                 |
| ------------------------- | ---------------------------------------------------- |
| ⏱ **Time Complexity**     | `O(n)` → In worst case (all 9s), traverse all digits |
| 💾 **Space Complexity**   | `O(1)` → In-place (except new digit added if all 9s) |
| ⚠️ **Edge Case Handling** | ✅ Covers all-9s scenario (`[9,9,9] → [1,0,0,0]`)     |

---

## ✅ Key Takeaways

* Simple **digit simulation** starting from the right.
* Efficient → `O(n)` time, `O(1)` space.
* Handles special case of **all 9s** cleanly.
* Works for both small and very large numbers stored as arrays.

---
