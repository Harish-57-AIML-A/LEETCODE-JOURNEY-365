Day 11: Longest Substring with At Most Two Distinct Characters

📌 **Difficulty**: 🔴 Hard

📌 **Frequency**: 📉 Rare

📌 **Link**: [🔗 LeetCode Problem](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)

---

## 📝 Problem Statement

Given a string `s`, find the **length of the longest substring** `T` that contains **at most two distinct characters**.

### 🔹 Example 1

* Input: `s = "eceba"`
* Output: `3`
* Explanation: The substring `"ece"` is the longest with at most two distinct characters.

### 🔹 Example 2

* Input: `s = "ccaabbb"`
* Output: `5`
* Explanation: The substring `"aabbb"` is the longest with at most two distinct characters.

---

## 💡 Approach

* Use the **sliding window technique** with two pointers (`i`, `j`).
* Maintain a **frequency map** of characters inside the current window.
* If the window exceeds **two distinct characters**, shrink it from the left until the condition is restored.
* Track the maximum window size during iteration.

⚡ This ensures each character is processed at most twice → runtime **O(n)**.

---

## 🐍 Python Solution

```python
def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    from collections import defaultdict
    
    count = defaultdict(int)
    i = 0
    max_len = 0
    
    for j, ch in enumerate(s):
        count[ch] += 1
        
        while len(count) > 2:
            count[s[i]] -= 1
            if count[s[i]] == 0:
                del count[s[i]]
            i += 1
        
        max_len = max(max_len, j - i + 1)
    
    return max_len


# 🚀 Example Run
print(lengthOfLongestSubstringTwoDistinct("eceba"))   # Output: 3
print(lengthOfLongestSubstringTwoDistinct("ccaabbb")) # Output: 5
```

---

## ☕ Java Solution

```java
import java.util.*;

class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int i = 0, maxLen = 0;

        for (int j = 0; j < s.length(); j++) {
            map.put(s.charAt(j), map.getOrDefault(s.charAt(j), 0) + 1);

            while (map.size() > 2) {
                map.put(s.charAt(i), map.get(s.charAt(i)) - 1);
                if (map.get(s.charAt(i)) == 0) {
                    map.remove(s.charAt(i));
                }
                i++;
            }
            maxLen = Math.max(maxLen, j - i + 1);
        }
        return maxLen;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.lengthOfLongestSubstringTwoDistinct("eceba"));   // 3
        System.out.println(sol.lengthOfLongestSubstringTwoDistinct("ccaabbb")); // 5
    }
}
```

---

## 📊 Complexity Analysis

| 🔎 Aspect               | 🐌 Brute Force                                           | ⚡ Sliding Window (Optimized)                            |
| ----------------------- | -------------------------------------------------------- | ------------------------------------------------------- |
| ⏱ **Time Complexity**   | `O(n³)` → Generate all substrings & check distinct chars | `O(n)` → Each character processed at most twice         |
| 💾 **Space Complexity** | `O(n)` → Extra storage for substring checks              | `O(1)` or `O(k)` → HashMap for at most 2 distinct chars |

---

✨ **Key Takeaways**

* 🚫 Brute force is too slow (`O(n³)`).
* ⚡ Sliding Window + HashMap makes it efficient (`O(n)`).
* 🔑 This problem generalizes to **"Longest Substring with At Most K Distinct Characters"**.

---
