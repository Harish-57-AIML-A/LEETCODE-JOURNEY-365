🌟 Day 12 - Missing Ranges

📌 **Difficulty**: 🟠 Medium

📌 **Frequency**: 📉 Medium

📌 **Link**: [🔗 LeetCode Problem](https://leetcode.com/problems/missing-ranges/)

---

## 📝 Problem Statement

You are given a **sorted integer array** where the range of elements is `[0, 99]` (inclusive).
Return the list of **missing ranges**.

---

## 🔹 Examples

### Example 1

**Input:** `nums = [0, 1, 3, 50, 75]`
**Output:** `["2", "4->49", "51->74", "76->99"]`

### Example 2

**Input:** `nums = []`
**Output:** `["0->99"]`

### Example 3

**Input:** `nums = [0, 1, 2, …, 99]`
**Output:** `[]`

---

## 💡 Approach

* Use **two pointers (`prev`, `curr`)** to track gaps.
* Add **artificial boundaries**:

  * `start - 1` before first element.
  * `end + 1` after last element.
* For every gap ≥ 2 → add missing range.
* Edge cases:

  * Empty array → return full `[start->end]`.
  * No missing → return empty list.

---

## 🐍 Python Solution

```python
from typing import List

def findMissingRanges(nums: List[int], start: int, end: int) -> List[str]:
    def get_range(low: int, high: int) -> str:
        return str(low) if low == high else f"{low}->{high}"

    ranges = []
    prev = start - 1
    nums.append(end + 1)  # Artificial boundary
    
    for curr in nums:
        if curr - prev >= 2:
            ranges.append(get_range(prev + 1, curr - 1))
        prev = curr

    return ranges


# 🚀 Example Run
print(findMissingRanges([0, 1, 3, 50, 75], 0, 99))  
# Output: ["2", "4->49", "51->74", "76->99"]
```

---

## ☕ Java Solution

```java
import java.util.*;

class Solution {
    public List<String> findMissingRanges(int[] nums, int start, int end) {
        List<String> ranges = new ArrayList<>();
        int prev = start - 1;

        for (int i = 0; i <= nums.length; i++) {
            int curr = (i == nums.length) ? end + 1 : nums[i];
            if (curr - prev >= 2) {
                ranges.add(getRange(prev + 1, curr - 1));
            }
            prev = curr;
        }
        return ranges;
    }

    private String getRange(int low, int high) {
        return (low == high) ? String.valueOf(low) : low + "->" + high;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.findMissingRanges(new int[]{0, 1, 3, 50, 75}, 0, 99));
        // Output: [2, 4->49, 51->74, 76->99]
    }
}
```

---

## 📊 Complexity Analysis

| Approach                   | ⏱ Time Complexity    | 💾 Space Complexity       | Notes                                  |
| -------------------------- | -------------------- | ------------------------- | -------------------------------------- |
| ❌ Brute Force              | `O(n * (end-start))` | `O(n)`                    | Iterates over full range, very slow    |
| ✅ Optimized (Two Pointers) | `O(n)`               | `O(1)` (excluding output) | Single pass with artificial boundaries |

---

## ✅ Key Takeaways

* Adding **artificial boundaries** simplifies logic.
* ⚡ Optimized solution runs in **linear time** relative to `nums`.
* 🚫 Brute force is inefficient for large ranges.

---
