📌 Problem 6: Reverse Words in a String  

🔗 **LeetCode Link:** [Reverse Words in a String](https://oj.leetcode.com/problems/reverse-words-in-a-string/)  
📊 **Difficulty:** Medium  
🔥 **Frequency:** High  

---

## 📝 Problem Statement  
Given an input string `s`, reverse the string **word by word**.  

👉 Notes:  
- A word is defined as a sequence of non-space characters.  
- Multiple spaces between words should be reduced to a **single space**.  
- The reversed string should not contain leading or trailing spaces.  
- Assume no tabs or newline characters.  

---

## 📖 Example  

**Input:**  
```text
s = "  the sky   is blue  "
````

**Output:**

```text
"blue is sky the"
```

**Explanation:**
After trimming and reducing multiple spaces, the words reversed are `"blue is sky the"`. ✅

---

## ⚙️ Approaches

### 1️⃣ Two-Pass Solution – O(n) Time, O(n) Space

* First pass → Split string into words.
* Second pass → Collect words in reverse order.

### 2️⃣ One-Pass Reverse Iteration – O(n) Time, O(n) Space ✅ Best Solution

* Iterate string **in reverse order**.
* Track each word’s **begin** and **end**.
* Append to result on the fly.

---

## 💻 Java Implementation

```java
public String reverseWords(String s) {
    StringBuilder reversed = new StringBuilder();
    int j = s.length();
    for (int i = s.length() - 1; i >= 0; i--) {
        if (s.charAt(i) == ' ') {
            j = i;
        } else if (i == 0 || s.charAt(i - 1) == ' ') {
            if (reversed.length() != 0) {
                reversed.append(' ');
            }
            reversed.append(s.substring(i, j));
        }
    }
    return reversed.toString();
}
```

---

## 🚀 Python Implementation

```python
def reverseWords(s: str) -> str:
    words = s.strip().split()
    return " ".join(reversed(words))

# Example Usage
print(reverseWords("  the sky   is blue  "))  # "blue is sky the"
print(reverseWords("hello world"))  # "world hello"
```

---

## 🔮 Follow-up

If the input string has:

* **No leading/trailing spaces**
* Words separated by a **single space**

👉 You can solve it **in-place** without extra space.
(This is covered in **Day 7 - Reverse Words in a String II**).

---

## ✅ OVERALL SUMMARY – Complexity Checklist

| Approach                 | Time Complexity | Space Complexity | Notes                         |
| ------------------------ | --------------- | ---------------- | ----------------------------- |
| Split + Reverse          | O(n)            | O(n)             | Simple & clean                |
| Reverse Iteration (Best) | O(n)            | O(n)             | Efficient one-pass solution ✅ |
| In-place (Follow-up)     | O(n)            | O(1)             | Possible if constraints apply |

```

