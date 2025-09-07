Day 11: Container With Most Water

📌 **Difficulty**: 🟠 Medium

📌 **Frequency**: 🔄 High

📌 **Link**: [🔗 LeetCode Problem](https://leetcode.com/problems/container-with-most-water/)

---

## 📝 Problem Statement

You are given an integer array `height` of length `n`.
Each element represents the **height of a vertical line** on the x-axis.

💡 **Task**: Find two lines that together with the x-axis form a container, such that the container holds the **most water**.

* ✅ Input: `height = [1,8,6,2,5,4,8,3,7]`
* ✅ Output: `49`
* ✅ Explanation: The lines at indices `1` and `8` form the container with **area = min(8,7) × (8-1) = 49**.

---

## 💡 Approach

* Start with **two pointers**: one at the leftmost (`l`) and one at the rightmost (`r`).
* At each step, calculate the **area** formed between the two lines.
* Move the pointer pointing to the **shorter line**, since moving the taller line won’t increase area.
* Continue until both pointers meet.

Efficiency:
⚡ Each index is checked **only once**, so runtime is **O(n)**.

---

## 🐍 Python Solution

```python
def maxArea(height):
    l, r = 0, len(height) - 1
    max_area = 0

    while l < r:
        area = min(height[l], height[r]) * (r - l)
        max_area = max(max_area, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area


# 🚀 Example Run
print(maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
```

---

## ☕ Java Solution

```java
class Solution {
    public int maxArea(int[] height) {
        int l = 0, r = height.length - 1;
        int maxArea = 0;

        while (l < r) {
            int area = Math.min(height[l], height[r]) * (r - l);
            maxArea = Math.max(maxArea, area);

            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return maxArea;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.maxArea(new int[]{1,8,6,2,5,4,8,3,7})); // 49
    }
}
```

---

## 📊 Complexity Analysis

| 🔎 Aspect               | 🐌 Brute Force Approach              | ⚡ Optimized Two-Pointer Approach |
| ----------------------- | ------------------------------------ | -------------------------------- |
| ⏱ **Time Complexity**   | **O(n²)** → Check all pairs of lines | **O(n)** → Each line visited ≤ 1 |
| 💾 **Space Complexity** | **O(1)** → Only variables            | **O(1)** → Two pointers only     |

---

✨ **Key Takeaways**

* 🐢 Brute Force → check every line pair → very slow.
* ⚡ Two-Pointer → greedy approach → optimal & linear.

---

👉 Do you want me to also prepare a **Day 11 sliding illustration (ASCII or diagram of shrinking container)** 🎨 so it matches your aesthetic GitHub series?

