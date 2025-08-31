📌 Problem 4: Valid Palindrome

🔗 LeetCode Link: Valid Palindrome

📊 Difficulty: Easy
🔥 Frequency: Medium

📝 Problem Statement

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

📖 Example

Input:

s = "A man, a plan, a canal: Panama"


Output:

true


Explanation:
After ignoring non-alphanumeric characters and case → "amanaplanacanalpanama" → palindrome ✅

Input:

s = "race a car"


Output:

false


Explanation:
Normalized string → "raceacar" → not a palindrome ❌

⚙️ Approach
1️⃣ Two-Pointer Technique – O(n) Time, O(1) Space ✅ Best Solution

Use two pointers i (start) and j (end).

Skip non-alphanumeric characters.

Compare characters in a case-insensitive way.

If mismatch → return false.

If pointers meet → palindrome true.
