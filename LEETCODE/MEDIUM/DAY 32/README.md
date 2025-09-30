🌟 Day 33 – Single Number

📌 **Difficulty**: 🟠 Medium

📌 **Frequency**: 🔥 High

📌 **Link**: [LeetCode – Single Number](https://oj.leetcode.com/problems/single-number/)

---

## 📝 Problem Statement

Given an array of integers, every element appears **twice except for one**. Find that single element.

---

## ❓ Example Questions Candidate Might Ask

* **Q:** Does the array contain both positive and negative integers?
  **A:** Yes.

* **Q:** Could any element appear more than twice?
  **A:** No, exactly one element appears only once, all others appear twice.

---

## 💡 Approaches

1. **Hash Map** → Count occurrences, then find the single one → `O(n)` time, `O(n)` space
2. **Set** → Add/remove elements to keep only the single element → `O(n)` time, `O(n)` space
3. **XOR Trick (Optimal)** → XOR all numbers → duplicates cancel out → `O(n)` time, `O(1)` space

---

## ☕ Java Solutions

### 🔹 Hash Map Approach – `O(n)` Space

```java
public int singleNumber(int[] A) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int x : A) {
        int count = map.containsKey(x) ? map.get(x) : 0;
        map.put(x, count + 1);
    }
    for (int x : A) {
        if (map.get(x) == 1) return x;
    }
    throw new IllegalArgumentException("No single element");
}
```

---

### 🔹 Set Approach – `O(n)` Space

```java
public int singleNumber(int[] A) {
    Set<Integer> set = new HashSet<>();
    for (int x : A) {
        if (set.contains(x)) set.remove(x);
        else set.add(x);
    }
    return set.iterator().next();
}
```

---

### 🔹 XOR Approach – `O(1)` Space ✅ Optimal

```java
public int singleNumber(int[] A) {
    int num = 0;
    for (int x : A) num ^= x;
    return num;
}
```

---

## 🐍 Python Solutions

### 🔹 Hash Map Approach – `O(n)` Space

```python
from collections import Counter

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = Counter(nums)
        for num, freq in count.items():
            if freq == 1:
                return num
```

---

### 🔹 Set Approach – `O(n)` Space

```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return s.pop()
```

---

### 🔹 XOR Approach – `O(1)` Space ✅ Optimal

```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
```

---

## 📊 Complexity Analysis

| Approach  | Time ⏱️ | Space 💾 |
| --------- | ------- | -------- |
| Hash Map  | O(n)    | O(n)     |
| Set       | O(n)    | O(n)     |
| XOR Trick | O(n)    | O(1)     |

---

## ✅ Key Takeaways

* ✅ **XOR Trick** leverages **commutative and associative** property → optimal solution.
* ✅ Set/Map solutions are intuitive but need **extra memory**.
* ✅ XOR approach can extend to problems like:

  * “Every element appears even number of times except one odd-count element”

---
