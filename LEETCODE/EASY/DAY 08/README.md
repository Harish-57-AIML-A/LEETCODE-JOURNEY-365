📌 Problem 8: String to Integer (atoi)  

🔗 **LeetCode Link:** [String to Integer (atoi)](https://oj.leetcode.com/problems/string-to-integer-atoi/)  
📊 **Difficulty:** Easy  
🔥 **Frequency:** High  

---

## 📝 Problem Statement  

Implement **atoi** to convert a string to an integer.  

The function works as follows:  
- Discards leading whitespace characters until the first non-whitespace character is found.  
- Takes an optional `'+'` or `'-'` sign.  
- Reads as many numerical digits as possible and interprets them as a number.  
- Ignores extra characters after the numeric portion.  
- Returns **0** if no valid conversion is performed.  
- If the number is out of range:  
  - Return `2147483647` (Integer.MAX_VALUE) if overflow.  
  - Return `-2147483648` (Integer.MIN_VALUE) if underflow.  

---

## 📖 Example  

**Input:**  
```text
"   -42"
````

**Output:**

```text
-42
```

**Explanation:**

* Discard leading spaces → `"-42"`
* Parse sign → `-`
* Parse digits → `42`
* Result → `-42 ✅`

---

## ⚙️ Approach – Handling Overflow

* Store the number while iterating digit by digit.
* At each step, check for **overflow / underflow** before multiplying by 10.
* Use a constant `maxDiv10 = Integer.MAX_VALUE / 10` to detect overflow early.

---

## 💻 Java Implementation

```java
private static final int maxDiv10 = Integer.MAX_VALUE / 10;

public int atoi(String str) {
    int i = 0, n = str.length();
    
    // Skip leading whitespaces
    while (i < n && Character.isWhitespace(str.charAt(i))) i++;
    
    // Handle sign
    int sign = 1;
    if (i < n && str.charAt(i) == '+') {
        i++;
    } else if (i < n && str.charAt(i) == '-') {
        sign = -1;
        i++;
    }
    
    // Convert digits
    int num = 0;
    while (i < n && Character.isDigit(str.charAt(i))) {
        int digit = Character.getNumericValue(str.charAt(i));
        
        // Handle overflow
        if (num > maxDiv10 || (num == maxDiv10 && digit >= 8)) {
            return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
        }
        
        num = num * 10 + digit;
        i++;
    }
    
    return sign * num;
}
```

---

## 🚀 Python Implementation

```python
def myAtoi(s: str) -> int:
    s = s.lstrip()  # remove leading whitespaces
    if not s:
        return 0
    
    # Handle sign
    sign = 1
    if s[0] in ['-', '+']:
        if s[0] == '-':
            sign = -1
        s = s[1:]
    
    # Convert digits
    num = 0
    for char in s:
        if not char.isdigit():
            break
        digit = int(char)
        
        # Handle overflow
        if num > (2**31 - 1) // 10 or (num == (2**31 - 1) // 10 and digit > 7):
            return (2**31 - 1) if sign == 1 else -(2**31)
        
        num = num * 10 + digit
    
    return sign * num

# Example Usage
print(myAtoi("   -42"))  # -42
```

---

## 🔮 Follow-up

* Can you implement this function without using built-in trimming or conversion helpers?
* What edge cases should be handled? (e.g., `"words123"`, `"   "`, `"+-12"`, `"2147483648"`).

---

## ✅ OVERALL SUMMARY – Complexity Checklist

| Operation         | Time Complexity | Space Complexity | Notes                         |
| ----------------- | --------------- | ---------------- | ----------------------------- |
| String Traversal  | O(n)            | O(1)             | One pass through the string   |
| Overflow Handling | O(1)            | O(1)             | Uses integer boundaries check |

```


