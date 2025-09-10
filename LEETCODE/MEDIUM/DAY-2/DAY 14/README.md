🌟 Day 14 - One Edit Distance

📌 **Difficulty**: 🟠 Medium
📌 **Frequency**: 📉 N/A
📌 **Link**: [🔗 LeetCode Problem](https://leetcode.com/problems/one-edit-distance/)

---

## 📝 Problem Statement

Given two strings **S** and **T**, determine if they are exactly **one edit distance apart**.

### Valid Operations (One Edit):

1. **Modify** → Change one character.

   * Example: `"abcde"` → `"abXde"`
2. **Insert** → Insert one character.

   * Example: `"abcde"` → `"abcXde"`
3. **Append** → Add one character at the end.

   * Example: `"abcde"` → `"abcdeX"`

---

## 🔹 Examples

### Example 1

**Input:** `s = "ab", t = "acb"`
**Output:** `True`
**Explanation:** Insert `"c"` in `s`.

### Example 2

**Input:** `s = "cab", t = "ad"`
**Output:** `False`
**Explanation:** More than one edit needed.

### Example 3

**Input:** `s = "1203", t = "1213"`
**Output:** `True`
**Explanation:** Modify `"0"` → `"1"`.

---

## 💡 Approach

* Let `m = len(s)`, `n = len(t)`.
* If `|m - n| > 1` → **impossible** (return False).
* Assume `m ≤ n` (swap if needed).
* Traverse both strings until a mismatch:

  * If lengths equal → check for **one modification**.
  * If lengths differ by 1 → check for **one insertion/append**.
* Finish traversal and validate no extra edits.

---

## 🐍 Python Solution

```python
def isOneEditDistance(s: str, t: str) -> bool:
    m, n = len(s), len(t)
    if m > n:
        return isOneEditDistance(t, s)
    if n - m > 1:
        return False

    i = 0
    while i < m and s[i] == t[i]:
        i += 1

    if i == m:
        return n - m == 1  # Extra char at end

    if m == n:
        i += 1  # Skip one mismatch

    while i < m and s[i] == t[i + (n - m)]:
        i += 1

    return i == m


# 🚀 Example Run
print(isOneEditDistance("ab", "acb"))   # True
print(isOneEditDistance("cab", "ad"))   # False
print(isOneEditDistance("1203", "1213")) # True
```

---

## ☕ Java Solution

```java
class Solution {
    public boolean isOneEditDistance(String s, String t) {
        int m = s.length(), n = t.length();
        if (m > n) return isOneEditDistance(t, s);
        if (n - m > 1) return false;

        int i = 0;
        while (i < m && s.charAt(i) == t.charAt(i)) i++;

        if (i == m) return n - m == 1; // Extra char at end

        if (m == n) i++; // Modification case

        while (i < m && s.charAt(i) == t.charAt(i + (n - m))) i++;

        return i == m;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isOneEditDistance("ab", "acb"));   // true
        System.out.println(sol.isOneEditDistance("cab", "ad"));   // false
        System.out.println(sol.isOneEditDistance("1203", "1213")); // true
    }
}
```

---

## 📊 Complexity Analysis

| 🔎 Aspect               | ⚡ Optimized One-Pass Approach        |
| ----------------------- | ------------------------------------ |
| ⏱ **Time Complexity**   | `O(n)` → Single traversal of strings |
| 💾 **Space Complexity** | `O(1)` → Constant extra space        |

---

## ✅ Key Takeaways

* 🚫 Avoid full **Edit Distance DP (`O(m*n)`)**, not needed here.
* ⚡ Single-pass linear solution is enough.
* Always **normalize lengths (m ≤ n)** to simplify cases.

---
