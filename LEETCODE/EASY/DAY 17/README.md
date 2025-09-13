🌟 Day 17 – Reverse Integer

📌 **Difficulty**: 🟢 Easy
📌 **Frequency**: 🔥 High
📌 **Link**: [🔗 LeetCode Problem](https://leetcode.com/problems/reverse-integer/)

---

## 📝 Problem Statement

Reverse the digits of an integer.

Examples:

* `x = 123` → `321`
* `x = -123` → `-321`
* `x = 10` → `1`

⚠️ Special case: If reversing causes **overflow/underflow** → return `0`.

---

## ❓ Example Questions Candidate Might Ask

* **Q:** What about negative integers?
  **A:** Just reverse digits and keep the sign (e.g., `-123 → -321`).

* **Q:** What about trailing zeros?
  **A:** They’re dropped (e.g., `100 → 1`).

* **Q:** What about overflow?
  **A:** If result exceeds `[-2³¹, 2³¹-1]`, return `0`.

---

## 💡 Approach

1. Extract last digit: `digit = x % 10`.
2. Add digit to result: `res = res * 10 + digit`.
3. Update input: `x //= 10`.
4. **Check overflow** before multiplying by 10.

---

## ☕ Java Solution

```java
public class Solution {
    public int reverse(int x) {
        int result = 0;

        while (x != 0) {
            int digit = x % 10;

            // Check overflow before updating result
            if (result > Integer.MAX_VALUE / 10 || result < Integer.MIN_VALUE / 10) {
                return 0;
            }

            result = result * 10 + digit;
            x /= 10;
        }

        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.reverse(123));     // 321
        System.out.println(sol.reverse(-123));    // -321
        System.out.println(sol.reverse(120));     // 21
        System.out.println(sol.reverse(1000000003)); // 0 (overflow)
    }
}
```

---

## 🐍 Python Solution

```python
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check overflow before adding
            if result > (2**31 - 1) // 10:
                return 0

            result = result * 10 + digit

        return sign * result


# 🚀 Example Run
sol = Solution()
print(sol.reverse(123))       # 321
print(sol.reverse(-123))      # -321
print(sol.reverse(120))       # 21
print(sol.reverse(1000000003)) # 0 (overflow)
```

---

## 📊 Complexity Analysis

| 🔎 Aspect                | ⚡ Optimized Approach                                      |
| ------------------------ | --------------------------------------------------------- |
| ⏱ **Time Complexity**    | `O(log₁₀(n))` → Processes each digit once                 |
| 💾 **Space Complexity**  | `O(1)` → Uses only constant variables                     |
| ⚠️ **Overflow Handling** | ✅ Checked before multiplying (`result * 10`) to stay safe |

---

## ✅ Key Takeaways

* Straightforward digit extraction using `%` and `//`.
* Overflow must be handled **before multiplying**.
* Works for both **positive and negative integers**.
* ⚡ Efficient → `O(log n)` time, `O(1)` space.

---
