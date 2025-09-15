🌟 Day 19 – Palindrome Number

📌 **Difficulty**: 🟢 Easy

📌 **Frequency**: 🔁 Medium

📌 **Link**: [🔗 LeetCode Problem](https://leetcode.com/problems/palindrome-number/)

---

## 📝 Problem Statement

Determine whether an integer is a **palindrome**. Do this **without extra space**.

**Examples**

* `121` → `true`
* `-121` → `false` (negative numbers are **not** palindromes here)
* `10` → `false` (`01` is not a valid representation)

---

## ❓ Candidate Clarifications (common)

* **Q:** Are negative numbers palindromes?
  **A:** **No** — for this problem negative ints are considered non-palindrome.
* **Q:** What about trailing zeros? e.g. `10` → `01` ?
  **A:** Not palindrome — leading zero after reverse is not allowed, so `10` → `false`.
* **Q:** Can I use string conversion?
  **A:** Yes it works, but it uses extra space — the interview asks to avoid extra space if possible.

---

## 💡 Approaches (short)

1. **String method** — convert to string and check reverse (simple, uses extra space).
2. **Reverse integer** — reverse the number and compare (watch out for overflow).
3. **Compare digits from both ends (no extra space)** — compute the highest divisor to extract the leading digit, compare with trailing digit, chop both ends and repeat. This is the recommended approach here.

---

## ☕ Java (recommended, no extra space)

```java
public class Solution {
    public boolean isPalindrome(int x) {
        // Negative numbers are not palindromes
        if (x < 0) return false;

        // Find the divisor to extract the leading digit
        int div = 1;
        while (x / div >= 10) {
            // watch out for overflow of div (but div stays <= 1e9 for 32-bit int)
            div *= 10;
        }

        while (x != 0) {
            int left = x / div;      // leading digit
            int right = x % 10;      // trailing digit
            if (left != right) return false;

            // remove leading and trailing digits
            x = (x % div) / 10;
            // removed two digits, so reduce divisor by factor 100
            div /= 100;
        }

        return true;
    }

    // quick tests
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.isPalindrome(121));    // true
        System.out.println(s.isPalindrome(-121));   // false
        System.out.println(s.isPalindrome(10));     // false
        System.out.println(s.isPalindrome(12321));  // true
    }
}
```

---

## 🐍 Python (recommended, no extra space)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative numbers are not palindromes
        if x < 0:
            return False

        # find divisor to get the leading digit
        div = 1
        while x // div >= 10:
            div *= 10

        while x:
            left = x // div
            right = x % 10
            if left != right:
                return False
            # remove leading and trailing digits
            x = (x % div) // 10
            div //= 100

        return True

# Example runs
sol = Solution()
print(sol.isPalindrome(121))    # True
print(sol.isPalindrome(-121))   # False
print(sol.isPalindrome(10))     # False
print(sol.isPalindrome(12321))  # True
```

---

## 📊 Complexity Analysis

| 🔎 Aspect               | ⚡ Digit-compare (no extra space)                                                                                         |   |      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------ | - | ---- |
| ⏱ **Time Complexity**   | **O(d)** where `d` = number of digits in `x` → \`O(log₁₀(                                                                | x | ))\` |
| 💾 **Space Complexity** | **O(1)** constant extra space                                                                                            |   |      |
| 📝 Notes                | This method avoids string allocation and integer-reverse overflow issues. String method would be O(d) time & O(d) space. |   |      |

---

## ✅ Key Takeaways

* Best interview solution: **compare digits from both ends using integer math** — no extra space, no overflow risk.
* Handle negatives immediately (`false`).
* Special-case: trailing zero numbers (like `10`) are **not** palindromes.
* Complexity is optimal: linear in number of digits (log of number value) and constant extra space.

---
