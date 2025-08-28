Got it 👍 You want a **unique and professional `README.md`** for your `two_sum` problem folder, instead of just dumping the raw text. I’ll structure it neatly with **sections, formatting, explanation, and code blocks** so it looks clean on GitHub.

Here’s a **refined version of your README**:

---

## 📌 Problem 1: Two Sum

🔗 **LeetCode Link:** [Two Sum](https://oj.leetcode.com/problems/two-sum/)
📊 **Difficulty:** Easy
🔥 **Frequency:** High

---

### 📝 Problem Statement

Given an array of integers, find **two numbers** such that they add up to a specific target number.

* The function `twoSum` should return the **indices** of the two numbers such that they add up to the target.
* The returned indices must be **1-based** (`index1 < index2`).
* You may assume that **exactly one solution** exists.

---

### 📖 Example

**Input:**

```text
numbers = [2, 7, 11, 15], target = 9
```

**Output:**

```text
[1, 2]
```

**Explanation:**
`numbers[0] + numbers[1] = 2 + 7 = 9`

---

### ⚙️ Approaches

#### 1. Brute Force – `O(n²)` runtime, `O(1)` space

* Loop through each element `x`.
* Check if there exists another element `target - x`.
* Requires nested loops → inefficient for large inputs.

```java
// Brute Force Solution
public int[] twoSum(int[] numbers, int target) {
    for (int i = 0; i < numbers.length; i++) {
        for (int j = i + 1; j < numbers.length; j++) {
            if (numbers[i] + numbers[j] == target) {
                return new int[]{i + 1, j + 1};
            }
        }
    }
    throw new IllegalArgumentException("No two sum solution");
}
```

---

#### 2. Optimized – Hash Table `O(n)` runtime, `O(n)` space

* Use a **hash map** to store values and their indices.
* For each element, check if `target - x` exists in the map.
* If yes → return indices.

```java
// Optimized Solution using HashMap
public int[] twoSum(int[] numbers, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < numbers.length; i++) {
        int x = numbers[i];
        if (map.containsKey(target - x)) {
            return new int[] { map.get(target - x) + 1, i + 1 };
        }
        map.put(x, i);
    }
    throw new IllegalArgumentException("No two sum solution");
}
```

---

### 🚀 Python Implementation

```python
def twoSum(numbers, target):
    num_map = {}
    for i, x in enumerate(numbers):
        complement = target - x
        if complement in num_map:
            return [num_map[complement] + 1, i + 1]
        num_map[x] = i
    raise ValueError("No two sum solution")
```

---

### 🔮 Follow-up

What if the input array is already sorted?
👉 Check [**Two Sum II – Input Array Is Sorted**](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

---

### ✅ Summary

* **Brute Force:** Easy to implement, but slow → `O(n²)`.
* **HashMap:** Much faster → `O(n)` runtime, `O(n)` space.
* **Sorted Input Case:** Can use **two pointers** for `O(n)` runtime and `O(1)` space.

---

Would you like me to also design a **template README format** that you can reuse for *every* problem (easy/medium/hard) so all your folders look consistent and professional on GitHub?

