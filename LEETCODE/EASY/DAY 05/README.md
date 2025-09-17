📌 Problem 5: Implement strstr()  

🔗 **LeetCode Link:** [Implement strstr()](https://oj.leetcode.com/problems/implement-strstr/)  
📊 **Difficulty:** Easy  
🔥 **Frequency:** High  

---

## 📝 Problem Statement  
Implement `strStr()`.  

Return the **index of the first occurrence** of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.  

👉 Notes:  
- If `needle` is empty → return `0`.  
- If `needle.length > haystack.length` → return `-1`.  
- Multiple occurrences → return the index of the **first match**.  

---

## 📖 Example  

**Input:**  
```text
haystack = "hello", needle = "ll"
```

**Output:**  
```text
2
```

**Explanation:**  
The substring `"ll"` starts at index `2`. ✅  

---

## ⚙️ Approaches  

### 1️⃣ Brute Force – O(nm) Time, O(1) Space ✅  

* Scan the `needle` with the `haystack` from each possible starting index.  
* Compare characters one by one.  
* If mismatch → shift to next index.  
* If full match → return index.  
* Covers all edge cases (empty strings, longer needle, multiple matches, etc.).  

---

## 💻 Java Implementation  

```java
public int strStr(String haystack, String needle) {
    for (int i = 0; ; i++) {
        for (int j = 0; ; j++) {
            if (j == needle.length()) return i;       // found match
            if (i + j == haystack.length()) return -1; // reached end
            if (needle.charAt(j) != haystack.charAt(i + j)) break; // mismatch
        }
    }
}
```

---

## 🚀 Python Implementation  

```python
def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
        else:
            return i
    return -1

# Example Usage
print(strStr("hello", "ll"))  # 2
print(strStr("aaaaa", "bba"))  # -1
```

---

## 🔮 Follow-up  

* For interviews, brute force is **enough**.  
* Advanced algorithms:  
  - **KMP (Knuth-Morris-Pratt)** → O(n + m)  
  - **Rabin-Karp** (rolling hash)  
  - **Boyer-Moore** (efficient in practice)  

These are usually taught in advanced algorithm classes.  

---

## ✅ OVERALL SUMMARY – Complexity Checklist  

| Approach        | Time Complexity | Space Complexity | Notes                           |
| --------------- | --------------- | ---------------- | ------------------------------- |
| Brute Force     | O(nm)           | O(1)             | Simple, clean, covers all cases |
| KMP Algorithm   | O(n + m)        | O(m)             | Efficient for long strings      |
| Rabin-Karp      | O(n + m) avg    | O(1)             | Uses rolling hash               |
| Boyer-Moore     | O(n/m) avg      | O(m)             | Very fast in practice           |

