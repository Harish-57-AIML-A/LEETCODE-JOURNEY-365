Day 9 – LeetCode: Valid Number

**🔗 Problem Link**: [Valid Number](https://leetcode.com/problems/valid-number/)
**📊 Difficulty**: 🟢 Easy
**🔥 Frequency**: 🔻 Low

---

## 📝 Problem Statement

Validate if a given string is **numeric**.

---

## ✅ Examples

| Input     | Output  | Explanation                     |
| --------- | ------- | ------------------------------- |
| `"0"`     | `true`  | Valid integer                   |
| `"0.1"`   | `true`  | Valid decimal                   |
| `"abc"`   | `false` | Contains non-numeric chars      |
| `"  1  "` | `true`  | Leading/trailing spaces ignored |
| `"1 1"`   | `false` | Spaces inside are invalid       |
| `"+1"`    | `true`  | Sign allowed                    |
| `"-1"`    | `true`  | Sign allowed                    |
| `"."`     | `false` | Needs at least one digit        |
| `"1."`    | `true`  | Equivalent to `1.0`             |
| `".1"`    | `true`  | Equivalent to `0.1`             |

---

## 🧩 Approach

1. Skip **leading spaces**
2. Handle **optional sign (+/-)**
3. Parse **integer part**
4. Parse **decimal part** (if exists)
5. Skip **trailing spaces**
6. Ensure at least **one digit exists**

---

## 🐍 Python Solution

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        i, n = 0, len(s)

        # Step 1: Skip leading whitespaces
        while i < n and s[i].isspace():
            i += 1

        # Step 2: Optional sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            i += 1

        is_numeric = False

        # Step 3: Integer part
        while i < n and s[i].isdigit():
            i += 1
            is_numeric = True

        # Step 4: Decimal part
        if i < n and s[i] == '.':
            i += 1
            while i < n and s[i].isdigit():
                i += 1
                is_numeric = True

        # Step 5: Skip trailing whitespaces
        while i < n and s[i].isspace():
            i += 1

        return is_numeric and i == n
```

---

## ☕ Java Solution

```java
public class Solution {
    public boolean isNumber(String s) {
        int i = 0, n = s.length();

        // Step 1: Skip leading whitespaces
        while (i < n && Character.isWhitespace(s.charAt(i))) i++;

        // Step 2: Optional sign
        if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) i++;

        boolean isNumeric = false;

        // Step 3: Integer part
        while (i < n && Character.isDigit(s.charAt(i))) {
            i++;
            isNumeric = true;
        }

        // Step 4: Decimal part
        if (i < n && s.charAt(i) == '.') {
            i++;
            while (i < n && Character.isDigit(s.charAt(i))) {
                i++;
                isNumeric = true;
            }
        }

        // Step 5: Skip trailing whitespaces
        while (i < n && Character.isWhitespace(s.charAt(i))) i++;

        return isNumeric && i == n;
    }
}
```

---

## 📦 Complexity Analysis

> 🕒 **Time Complexity**

```
O(n)
✔ Each character is checked at most once
```

> 💾 **Space Complexity**

```
O(1)
✔ Uses only pointers/flags
```

---

## 🌟 Key Takeaways

* Trim **leading/trailing spaces**
* Allow **+ / -** signs
* Must contain **at least one digit**
* Handle **decimal numbers properly**

---

Perfect 👍 you want the **Complexity Analysis** to be **structured**, clean, and aesthetic — not just text inside quotes.

Here’s how we can format it for **Day 9 – Valid Number**:

---

## 📦 Complexity Analysis

| Language  | Time Complexity | Space Complexity | Explanation                                           |
| --------- | --------------- | ---------------- | ----------------------------------------------------- |
| 🐍 Python | 🕒 `O(n)`       | 💾 `O(1)`        | Each character checked once, uses only pointers/flags |
| ☕ Java    | 🕒 `O(n)`       | 💾 `O(1)`        | Linear scan of string, no extra data structures       |

---

✅ This format gives a **side-by-side structured view** with icons, code-like boxes for complexity, and a clear explanation.

---
