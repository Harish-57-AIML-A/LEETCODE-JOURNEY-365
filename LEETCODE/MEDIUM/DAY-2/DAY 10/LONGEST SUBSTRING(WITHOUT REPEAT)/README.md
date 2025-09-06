Got it 🚀 You want a **Day 10 README file** for the problem *Longest Substring Without Repeating Characters*, with:

* **Problem statement**
* **Python + Java code**
* **Comparative Complexity Analysis in structured box format (like a table/box)**

Here’s the structured content:

---

# 📘 Day 10: Longest Substring Without Repeating Characters

**Difficulty**: Medium
**Frequency**: Medium
**Link**: [LeetCode – Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## 🔹 Problem Statement

Given a string, find the length of the longest substring without repeating characters.

**Example 1**

```
Input: "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring.
```

**Example 2**

```
Input: "bbbbb"
Output: 1
Explanation: "b" is the longest substring.
```

**Example 3**

```
Input: "pwwkew"
Output: 3
Explanation: "wke" is the longest substring.
```

---

## 🔹 Approach

We use a **sliding window technique** with two pointers (`i` = start, `j` = end).

* Use a hash map (or array for ASCII) to keep track of characters and their indices.
* When a repeating character is found, shift the start pointer `i` just past the last occurrence of that character.
* Keep track of the maximum window size.

This guarantees **O(n)** runtime since each character is visited at most twice.

---

## 🔹 Python Solution

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


# Example Run
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3
```

---

## 🔹 Java Solution

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

    // Example Run
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.lengthOfLongestSubstring("abcabcbb")); // 3
        System.out.println(sol.lengthOfLongestSubstring("bbbbb"));    // 1
        System.out.println(sol.lengthOfLongestSubstring("pwwkew"));   // 3
    }
}
```

---

## 🔹 Complexity Analysis

| Aspect               | Brute Force Approach                | Optimized Sliding Window                                              |
| -------------------- | ----------------------------------- | --------------------------------------------------------------------- |
| **Time Complexity**  | **O(n²)** (checking all substrings) | **O(n)** (each character visited at most twice)                       |
| **Space Complexity** | **O(1)** (no extra storage)         | **O(min(n, charset))** → ASCII: **O(256) \~ O(1)**, Unicode: **O(n)** |

---

📌 **Key Insight**:

* Brute force checks all substrings (slow).
* Sliding window efficiently skips unnecessary checks → **linear scan only**.

---

Do you want me to also make this into a **ready-to-use `README.md` file** with markdown formatting (like for your daily repo), so you can directly push it to GitHub?

