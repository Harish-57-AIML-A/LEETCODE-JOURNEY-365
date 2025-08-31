````markdown
# 🚀 LeetCode Journey – Day 4  

## 📌 Problem: Valid Palindrome  
🔗 **Link:** [Valid Palindrome](https://oj.leetcode.com/problems/valid-palindrome/)  
📊 **Difficulty:** Easy  
🔥 **Frequency:** Medium  

---

### 📝 Question  
Given a string, determine if it is a **palindrome**, considering only **alphanumeric characters** and ignoring cases.  

**Examples:**  
- `"A man, a plan, a canal: Panama"` ➝ ✅ Palindrome  
- `"race a car"` ➝ ❌ Not a palindrome  

**Note:**  
- An **empty string** is considered a valid palindrome.  

---

### ❓ Example Interview Question  
**Q:** What about an empty string? Is it a valid palindrome?  
**A:** Yes, for this problem, an empty string is a valid palindrome.  

---

### 💡 Solution Approach  
- Use **two pointers**: one starting from the **head** and the other from the **tail**.  
- Move both pointers towards the center, skipping **non-alphanumeric characters**.  
- Compare characters in a **case-insensitive** manner.  
- If all match → it's a palindrome ✅, otherwise ❌.  

⏱ **Time Complexity:** `O(n)`  
📦 **Space Complexity:** `O(1)`  

---

### 🐍 Python Solution
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
````

---

✅ **Key Takeaways:**

* Palindrome check must **ignore cases**.
* Must handle **non-alphanumeric characters**.
* Edge case: **Empty string is valid**.

---



