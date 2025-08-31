Here’s your Day 4 README:

# 📌 Problem 4: Valid Palindrome  

🔗 **LeetCode Link:** [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)  
📊 **Difficulty:** Easy  
🔥 **Frequency:** Medium  

---

## 📝 Problem Statement  
Given a string, determine if it is a **palindrome**, considering only **alphanumeric characters** and ignoring cases.  

- Example 1: `"A man, a plan, a canal: Panama"` → ✅ Palindrome  
- Example 2: `"race a car"` → ❌ Not a Palindrome  

👉 **Note**: An **empty string** is considered a valid palindrome.  

---

## 📖 Example  

**Input:**  
```text
s = "A man, a plan, a canal: Panama"
```

**Output:**  
```text
true
```

**Explanation:**  
After removing non-alphanumeric characters and ignoring cases,  
`"amanaplanacanalpanama"` is a palindrome. ✅  

---

## ⚙️ Approaches  

### 1️⃣ Two Pointers – O(n) Time, O(1) Space ✅ Best Solution  

* Use two pointers (`i` at start, `j` at end).  
* Skip all non-alphanumeric characters.  
* Compare characters in lowercase.  
* If all match → return true.  
* If any mismatch → return false.  

---

## 💻 Java Implementation  

```java
public boolean isPalindrome(String s) {
    int i = 0, j = s.length() - 1;
    while (i < j) {
        while (i < j && !Character.isLetterOrDigit(s.charAt(i))) i++;
        while (i < j && !Character.isLetterOrDigit(s.charAt(j))) j--;
        if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) {
            return false;
        }
        i++; j--;
    }
    return true;
}
```

---

## 🚀 Python Implementation  

```python
def isPalindrome(s: str) -> bool:
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

# Example Usage
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))  # False
```

---

## 🔮 Follow-up  

* The **two-pointer** approach works best with O(1) space.  
* Alternative: preprocess string (keep only alphanumeric, lowercase it) → then check if string equals its reverse.  
* But that uses O(n) extra space.  

---

## ✅ OVERALL SUMMARY – Complexity Checklist  

| Approach                     | Time Complexity | Space Complexity | Notes                        |
| ---------------------------- | --------------- | ---------------- | ---------------------------- |
| Preprocess + Reverse Compare | O(n)            | O(n)             | Simple but uses extra space  |
| Two Pointers (Best)          | O(n)            | O(1)             | Efficient and optimal ✅      |
