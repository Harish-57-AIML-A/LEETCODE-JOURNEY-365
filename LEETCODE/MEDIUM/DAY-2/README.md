Perfect 👍 I’ve refactored your provided draft into a **unique, professional, GitHub-ready README** in the exact style you wanted for *Problem 2: Two Sum II – Input Array Is Sorted*.

Here’s the clean version:

````markdown
# 📌 Problem 2: Two Sum II – Input Array Is Sorted  

🔗 **LeetCode Link:** [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)  
📊 **Difficulty:** Medium  
🔥 **Frequency:** High  

---

## 📝 Problem Statement  
Given a **1-indexed sorted array** of integers `numbers`, return the indices of the two numbers such that they add up to a specific target number.  

**Constraints:**  
- Each input has exactly one solution.  
- You may not use the same element twice.  
- Indices must be returned in **ascending order**.  

---

## 📖 Example  

**Input:**  
```text
numbers = [2, 7, 11, 15], target = 9
````

**Output:**

```text
[1, 2]
```

**Explanation:**
`numbers[0] + numbers[1] = 2 + 7 = 9`

---

## ⚙️ Approaches

### 1️⃣ Binary Search – `O(n log n)` runtime, `O(1)` space

* For each element `x`, search for `target - x` using binary search.
* Works, but does **not fully exploit the sorted nature** of the input.

```java
public int[] twoSum(int[] numbers, int target) {
    for (int i = 0; i < numbers.length; i++) {
        int j = bsearch(numbers, target - numbers[i], i + 1);
        if (j != -1) {
            return new int[]{i + 1, j + 1};
        }
    }
    throw new IllegalArgumentException("No two sum solution");
}

private int bsearch(int[] A, int key, int start) {
    int L = start, R = A.length - 1;
    while (L < R) {
        int M = (L + R) / 2;
        if (A[M] < key) {
            L = M + 1;
        } else {
            R = M;
        }
    }
    return (L == R && A[L] == key) ? L : -1;
}
```

---

### 2️⃣ Two Pointers – `O(n)` runtime, `O(1)` space ✅ Best Solution

* Use two indices `i` (start) and `j` (end).
* If `numbers[i] + numbers[j] < target`, move `i` forward.
* If `numbers[i] + numbers[j] > target`, move `j` backward.
* If equal → found solution.

```java
public int[] twoSum(int[] numbers, int target) {
    int i = 0, j = numbers.length - 1;
    while (i < j) {
        int sum = numbers[i] + numbers[j];
        if (sum < target) {
            i++;
        } else if (sum > target) {
            j--;
        } else {
            return new int[]{i + 1, j + 1};
        }
    }
    throw new IllegalArgumentException("No two sum solution");
}
```

---

## 🚀 Python Implementation

```python
def twoSum(numbers, target):
    i, j = 0, len(numbers) - 1
    while i < j:
        s = numbers[i] + numbers[j]
        if s < target:
            i += 1
        elif s > target:
            j -= 1
        else:
            return [i + 1, j + 1]
    raise ValueError("No two sum solution")
```

---

## 🔮 Follow-up

* The **Two Pointers** method leverages the sorted nature of the input.
* If the array were **unsorted**, we’d need to use a **HashMap** (like in **Problem 1: Two Sum**).

---

## ✅ OVERALL SUMMARY – Complexity Checklist

| Approach      | Time Complexity | Space Complexity | Notes                   |
| ------------- | --------------- | ---------------- | ----------------------- |
| Binary Search | O(n log n)      | O(1)             | Uses extra search step  |
| Two Pointers  | O(n)            | O(1)             | Best & most efficient ✅ |

---

```

👉 This is **unique, professional, and cleanly structured** — much better than raw dumps.  

Do you want me to now **generalize this into a README template** (with placeholders like *Problem X, Example, Java/Python code, Summary*) so that for every new problem (Easy/Medium/Hard), you can just plug in details without rewriting the structure?
```
