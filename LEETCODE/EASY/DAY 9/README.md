Day 9 – LeetCode: Valid Number

**Problem Link**: [Valid Number](https://leetcode.com/problems/valid-number/)
**Difficulty**: 🟢 Easy
**Frequency**: 🔻 Low

---

## 📌 Problem Statement

Validate if a given string is **numeric**.

### ✅ Examples

| Input     | Output  | Explanation                          |
| --------- | ------- | ------------------------------------ |
| `"0"`     | `true`  | Valid integer                        |
| `"0.1"`   | `true`  | Valid decimal                        |
| `"abc"`   | `false` | Contains non-numeric chars           |
| `"  1  "` | `true`  | Leading/trailing whitespaces ignored |
| `"1 1"`   | `false` | Spaces inside are invalid            |
| `"+1"`    | `true`  | Sign allowed                         |
| `"-1"`    | `true`  | Sign allowed                         |
| `"."`     | `false` | Needs at least one digit             |
| `"1."`    | `true`  | Equivalent to `1.0`                  |
| `".1"`    | `true`  | Equivalent to `0.1`                  |

---

## ❓ Candidate Clarifications

* **Q:** Should I ignore leading/trailing spaces?
  **A:** ✅ Yes
* **Q:** Can spaces exist inside?
  **A:** ❌ No, `"1 1"` is invalid.
* **Q:** Are signs (+/-) valid?
  **A:** ✅ Yes, at the beginning.
* **Q:** Hexadecimal like `0xFF` valid?
  **A:** ❌ No, only decimal numbers.
* **Q:** Exponent like `1e10`?
  **A:** ❌ Not for this version (but LC problem considers exponent).

---

## 🧩 Approach

We divide the string into logical segments:

1. **Leading spaces** → ignore
2. **Sign (+/-)** → optional
3. **Integer / Decimal** → must exist
4. **Trailing spaces** → ignore

### Rules:

* Whole numbers must contain **only digits**.
* Decimal numbers can be split as:

  * **Integer part** (optional)
  * **Decimal point** `.` (mandatory if decimal)
  * **Fractional part** (optional)
* At least one digit must exist (`"."` alone is invalid).

---

## 🧑‍💻 Code (Java)

```java
public class ValidNumber {
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

        // Final check
        return isNumeric && i == n;
    }
}
```

---

## 🕒 Complexity Analysis

* **Time Complexity:** `O(n)` → iterate through string once
* **Space Complexity:** `O(1)` → constant extra space

---

## 🌟 Key Takeaways

* Handle **corner cases** (`+`, `-`, `.`, `"   "`).
* A valid number must have **at least one digit**.
* Separate handling of **whitespaces** is crucial.

---

