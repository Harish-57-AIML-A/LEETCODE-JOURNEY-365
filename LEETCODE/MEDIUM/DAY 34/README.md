🌟 Day 35 – Spiral Matrix

📌 **Difficulty**: 🟠 Medium

📌 **Frequency**: ⚡ Medium

📌 **Link**: [LeetCode – Spiral Matrix](https://oj.leetcode.com/problems/spiral-matrix)

---

## 📝 Problem Statement

Given a matrix of `m × n` elements (m rows, n columns), return **all elements of the matrix in spiral order**.

**Example**:

```text
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output: [1,2,3,6,9,8,7,4,5]
```

---

## 💡 Idea / Solution

* We **simulate walking the matrix** in a spiral manner:

  1. Move **right** → `n` steps
  2. Move **down** → `m-1` steps
  3. Move **left** → `n-1` steps
  4. Move **up** → `m-2` steps
  5. Repeat for inner layers until all elements are visited.
* Keep track of **current position** and **remaining steps** in each direction.
* Handle **edge cases** like 1×1, 1×n, n×1 matrices separately.

---

## ☕ Java Solution

```java
public List<Integer> spiralOrder(int[][] matrix) {
    List<Integer> elements = new ArrayList<>();
    if (matrix.length == 0) return elements;
    
    int m = matrix.length, n = matrix[0].length;
    int row = 0, col = -1;
    
    while (true) {
        for (int i = 0; i < n; i++) elements.add(matrix[row][++col]);
        if (--m == 0) break;
        
        for (int i = 0; i < m; i++) elements.add(matrix[++row][col]);
        if (--n == 0) break;
        
        for (int i = 0; i < n; i++) elements.add(matrix[row][--col]);
        if (--m == 0) break;
        
        for (int i = 0; i < m; i++) elements.add(matrix[--row][col]);
        if (--n == 0) break;
    }
    
    return elements;
}
```

---

## 🐍 Python Solution

```python
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix: return []
        elements = []
        m, n = len(matrix), len(matrix[0])
        row, col = 0, -1
        
        while True:
            for _ in range(n):
                col += 1
                elements.append(matrix[row][col])
            m -= 1
            if m == 0: break
            
            for _ in range(m):
                row += 1
                elements.append(matrix[row][col])
            n -= 1
            if n == 0: break
            
            for _ in range(n):
                col -= 1
                elements.append(matrix[row][col])
            m -= 1
            if m == 0: break
            
            for _ in range(m):
                row -= 1
                elements.append(matrix[row][col])
            n -= 1
            if n == 0: break
        
        return elements
```

---

## 📊 Complexity Analysis

| Approach        | Time ⏱️ | Space 💾 |
| --------------- | ------- | -------- |
| Simulation Walk | O(m*n)  | O(1)     |

---

## ✅ Key Takeaways

* ✅ Spiral traversal can be done **layer by layer**.
* ✅ Maintain **remaining steps** in each direction to avoid over-traversing.
* ✅ Works for **non-square matrices** (rectangular matrices) as well.

---
