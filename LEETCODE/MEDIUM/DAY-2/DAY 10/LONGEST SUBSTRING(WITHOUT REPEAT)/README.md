🌟 Day 10: Longest Substring Without Repeating Characters

📌 **Difficulty**: 🟠 Medium
📌 **Frequency**: 🔄 Medium
📌 **Link**: [🔗 LeetCode Problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## 📝 Problem Statement

Given a string, find the **length of the longest substring without repeating characters**.

💡 **Examples**:

* ✅ Input: `"abcabcbb"` → Output: `3` → Substring: `"abc"`
* ✅ Input: `"bbbbb"` → Output: `1` → Substring: `"b"`
* ✅ Input: `"pwwkew"` → Output: `3` → Substring: `"wke"`

---

## 💡 Approach

We use a **Sliding Window** 📏 with two pointers:

* 🔹 Maintain a **map/dictionary** to store the last seen index of each character.
* 🔹 If a repeating character is found → shift the start pointer `i` 👉 to `last_index + 1`.
* 🔹 Keep updating the **max window length**.

Efficiency:
⚡ Each character is visited **at most twice** → **O(n)** runtime.

---

## 🐍 Python Solution

```python
def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    i = 0
    max_len = 0

    for j in range(len(s)):
        if s[j] in char_map and char_map[s[j]] >= i:
            i = char_map[s[j]] + 1
        char_map[s[j]] = j
        max_len = max(max_len, j - i + 1)

    return max_len


# 🚀 Example Runs
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3
```

---

## ☕ Java Solution

```java
import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> charMap = new HashMap<>();
        int i = 0, maxLen = 0;

        for (int j = 0; j < s.length(); j++) {
            if (charMap.containsKey(s.charAt(j)) && charMap.get(s.charAt(j)) >= i) {
                i = charMap.get(s.charAt(j)) + 1;
            }
            charMap.put(s.charAt(j), j);
            maxLen = Math.max(maxLen, j - i + 1);
        }

        return maxLen;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.lengthOfLongestSubstring("abcabcbb")); // 3
        System.out.println(sol.lengthOfLongestSubstring("bbbbb"));    // 1
        System.out.println(sol.lengthOfLongestSubstring("pwwkew"));   // 3
    }
}
```

---

## 📊 Complexity Analysis

| 🔎 Aspect               | 🐌 Brute Force Approach          | ⚡ Optimized Sliding Window                                             |
| ----------------------- | -------------------------------- | ---------------------------------------------------------------------- |
| ⏱ **Time Complexity**   | **O(n²)** → check all substrings | **O(n)** → each char visited ≤ 2                                       |
| 💾 **Space Complexity** | **O(1)** (no extra storage)      | **O(min(n, charset))** → ASCII = **O(256) ≈ O(1)**, Unicode = **O(n)** |

---

✨ **Key Takeaways**

* 🐢 Brute Force → checks **every substring** (inefficient).
* ⚡ Sliding Window → **smart skip** of duplicates = **linear scan only**.

---
