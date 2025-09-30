🌟 Day 34 – Single Number II

📌 **Difficulty**: 🔴 Hard

📌 **Frequency**: ⚡ Medium

📌 **Link**: [LeetCode – Single Number II](https://oj.leetcode.com/problems/single-number-ii)

---

## 📝 Problem Statement

Given an array of integers, **every element appears three times except for one**. Find that single one.

⚠️ **Constraint**: Your algorithm should run in **linear time** and use **constant space**.

---

## 💡 Idea / Solution

* A number in a computer is represented using **bits**.
* If we sum the **i-th bit** of all numbers and mod 3, the result gives the **i-th bit** of the single number.
* This leads to two main approaches:

  1. **Bit count array (O(32*n) time, O(1) space)**
  2. **Bitmask variables (ones, twos, threes) – optimal solution using constant space**

---

## ☕ Java Solutions

### 🔹 Bit Count Array – Simple Approach

```java
public int singleNumber(int[] nums) {
    int[] count = new int[32];
    int result = 0;
    for (int i = 0; i < 32; i++) {
        for (int num : nums) {
            if (((num >> i) & 1) == 1) count[i]++;
        }
        result |= (count[i] % 3) << i;
    }
    return result;
}
```

---

### 🔹 Bitmask Variables – Optimal Approach ✅

```java
public int singleNumber(int[] nums) {
    int ones = 0, twos = 0, threes = 0;
    for (int num : nums) {
        twos |= ones & num;
        ones ^= num;
        threes = ones & twos;
        ones &= ~threes;
        twos &= ~threes;
    }
    return ones;
}
```

---

## 🐍 Python Solutions

### 🔹 Bit Count Array – Simple Approach

```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = [0] * 32
        result = 0
        for i in range(32):
            for num in nums:
                if (num >> i) & 1:
                    count[i] += 1
            result |= (count[i] % 3) << i
        # Handle negative numbers
        if result >= 2**31:
            result -= 2**32
        return result
```

---

### 🔹 Bitmask Variables – Optimal Approach ✅

```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = twos = 0
        for num in nums:
            twos |= ones & num
            ones ^= num
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones
```

---

## 📊 Complexity Analysis

| Approach          | Time ⏱️        | Space 💾 |
| ----------------- | -------------- | -------- |
| Bit Count Array   | O(32*n) ≈ O(n) | O(1)     |
| Bitmask Variables | O(n)           | O(1)     |

---

## ✅ Key Takeaways

* ✅ **Bit manipulation** is powerful for problems with numbers appearing multiple times.
* ✅ Bitmask variables approach is **optimal in space and time**.
* ✅ This technique can be generalized to cases like:

  * Every element appears **k times except one**
  * Use **k-bit tracking logic**

---
