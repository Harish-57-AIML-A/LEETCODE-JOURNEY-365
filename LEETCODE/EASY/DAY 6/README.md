📌 Problem 6: Reverse Words in a String

🔗 LeetCode Link: Reverse Words in a String

📊 Difficulty: Medium
🔥 Frequency: High

📝 Problem Statement

Given an input string s, reverse the string word by word.

👉 Notes:

A word is a sequence of non-space characters.

Input may contain leading/trailing spaces → remove them in result.

Multiple spaces between words → reduce to a single space in result.

📖 Example

Input:

s = "  the sky   is blue "


Output:

"blue is sky the"


Explanation:
After trimming spaces and reversing → "blue is sky the". ✅

⚙️ Approaches
1️⃣ Two-Pass Approach – O(n) Time, O(n) Space

Split string by spaces.

Filter out empty entries.

Join words in reverse order.

2️⃣ One-Pass Reverse Iteration – O(n) Time, O(n) Space ✅ (More Optimal)

Iterate from end to start.

Track word boundaries.

Append words directly in reverse order.

💻 Java Implementation
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

🚀 Python Implementation
def reverseWords(s: str) -> str:
    words = s.strip().split()
    return " ".join(reversed(words))

# Example Usage
print(reverseWords("  the sky   is blue "))  # "blue is sky the"
print(reverseWords("hello world"))           # "world hello"

🔮 Follow-up

If input string contains no leading/trailing spaces and words are separated by a single space,
👉 The problem can be solved in-place without allocating extra space (see Problem 7: Reverse Words in a String II).

✅ OVERALL SUMMARY – Complexity Checklist
Approach	Time Complexity	Space Complexity	Notes
Split + Reverse (Simple)	O(n)	O(n)	Easiest, uses extra array
One-Pass Reverse (Better)	O(n)	O(n)	Avoids unnecessary splitting
In-Place (Follow-up)	O(n)	O(1)	Possible if constraints allow
