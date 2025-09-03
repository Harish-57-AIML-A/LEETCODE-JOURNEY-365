 📌 Problem 7: Reverse Words in a String II  

🔗 **LeetCode Link:** [Reverse Words in a String II](https://oj.leetcode.com/problems/reverse-words-in-a-string-ii/)  
📊 **Difficulty:** Medium  
🔥 **Frequency:** N/A  

---

## 📝 Problem Statement  
Similar to **[6. Reverse Words in a String]**, but with the following constraints:  

👉 Notes:  
- The input string does **not** contain leading or trailing spaces.  
- Words are always separated by a **single space**.  
- Could you do it **in-place** without allocating extra space?  

---

## 📖 Example  

**Input:**  
```text
s = "the sky is blue"
Output:

text
Copy code
"blue is sky the"
Explanation:
The words are reversed in-place, using O(1) extra space. ✅

⚙️ Approaches
1️⃣ In-place Reverse – O(n) Time, O(1) Space ✅
Reverse the entire string → wn' … w2' w1'.

Reverse each word individually → wn … w2 w1.

Achieves the result without extra space.

💻 Java Implementation
java
Copy code
public void reverseWords(char[] s) {
    reverse(s, 0, s.length);
    for (int i = 0, j = 0; j <= s.length; j++) {
        if (j == s.length || s[j] == ' ') {
            reverse(s, i, j);
            i = j + 1;
        }
    }
}

private void reverse(char[] s, int begin, int end) {
    for (int i = 0; i < (end - begin) / 2; i++) {
        char temp = s[begin + i];
        s[begin + i] = s[end - i - 1];
        s[end - i - 1] = temp;
    }
}
🚀 Python Implementation
python
Copy code
def reverseWords(s: list) -> None:
    def reverse(l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1

    # Step 1: Reverse entire string
    reverse(0, len(s) - 1)

    # Step 2: Reverse each word
    i = 0
    for j in range(len(s) + 1):
        if j == len(s) or s[j] == ' ':
            reverse(i, j - 1)
            i = j + 1

# Example Usage
chars = list("the sky is blue")
reverseWords(chars)
print("".join(chars))  # "blue is sky the"
🔮 Follow-up
Challenge 1:
Implement the two-pass solution without using the library’s split function.

Challenge 2:
Rotate an array to the right by k steps in-place without allocating extra space.

👉 Example:
For k = 3, the array

text
Copy code
[0, 1, 2, 3, 4, 5, 6]
becomes

text
Copy code
[4, 5, 6, 0, 1, 2, 3]
✅ OVERALL SUMMARY – Complexity Checklist
Approach	Time Complexity	Space Complexity	Notes
In-place Reverse	O(n)	O(1)	Efficient, no extra memory used ✅
Two-Pass (No split)	O(n)	O(1)	Alternate method without library
Array Rotation	O(n)	O(1)	Related challenge extension
