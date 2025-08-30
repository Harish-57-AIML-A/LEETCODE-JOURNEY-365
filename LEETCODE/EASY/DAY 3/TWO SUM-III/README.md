Here’s your Day 3 README:

# 📌 Problem 3: Two Sum III – Data Structure Design  

🔗 **LeetCode Link:** [Two Sum III](https://leetcode.com/problems/two-sum-iii-data-structure-design/)  
📊 **Difficulty:** Easy  
🔥 **Frequency:** Medium  

---

## 📝 Problem Statement  
Design and implement a **TwoSum** class that supports the following operations:  

- `add(input)` → Add the number `input` to an internal data structure.  
- `find(value)` → Find if there exists **any pair of numbers** whose sum is equal to `value`.  

---

## 📖 Example  

**Input / Operations:**  
```text
add(1)
add(3)
add(5)
find(4) → true
find(7) → false


Explanation:

**Explanation:**

* 1 + 3 = 4 → found ✅
* No pair sums to 7 → false ❌

---

## ⚙️ Approaches

### 1️⃣ Store All Pair Sums – O(n²) Space, Fast Find

* Maintain a hash table of all possible pair sums.
* `add`: For each new element, form sums with existing numbers → O(n).
* `find`: Simply check if the value exists in hash table → O(1).
* Useful if `find` is called much more frequently than `add`.

---

### 2️⃣ Sorted Array + Two Pointers – O(log n) Add, O(n) Find

* Keep numbers in sorted order.
* `add`: Insert in O(log n) using binary search.
* `find`: Use **two pointers** to check if a pair sums to target.
* More space-efficient than storing all pair sums.

---

### 3️⃣ Hash Table (Best Trade-off) – O(1) Add, O(n) Find ✅

* Store numbers and their counts in a HashMap.
* `add`: Increment count → O(1).
* `find`: Iterate through keys, check if `(target - num)` exists.

  * Special case: if `num == target - num`, need count ≥ 2.

---

## 💻 Java Implementation

```java
class TwoSum {
    private Map<Integer, Integer> table = new HashMap<>();
    
    // Add number to the data structure
    public void add(int number) {
        int count = table.getOrDefault(number, 0);
        table.put(number, count + 1);
    }
    
    // Find if there exists a pair with given sum
    public boolean find(int value) {
        for (Map.Entry<Integer, Integer> entry : table.entrySet()) {
            int num = entry.getKey();
            int y = value - num;
            if (y == num) {
                if (entry.getValue() >= 2) return true;
            } else if (table.containsKey(y)) {
                return true;
            }
        }
        return false;
    }
}
```

**Explanation:**

* 1 + 3 = 4 → found ✅
* No pair sums to 7 → false ❌

---

## ⚙️ Approaches

### 1️⃣ Store All Pair Sums – O(n²) Space, Fast Find

* Maintain a hash table of all possible pair sums.
* `add`: For each new element, form sums with existing numbers → O(n).
* `find`: Simply check if the value exists in hash table → O(1).
* Useful if `find` is called much more frequently than `add`.

---

### 2️⃣ Sorted Array + Two Pointers – O(log n) Add, O(n) Find

* Keep numbers in sorted order.
* `add`: Insert in O(log n) using binary search.
* `find`: Use **two pointers** to check if a pair sums to target.
* More space-efficient than storing all pair sums.

---

### 3️⃣ Hash Table (Best Trade-off) – O(1) Add, O(n) Find ✅

* Store numbers and their counts in a HashMap.
* `add`: Increment count → O(1).
* `find`: Iterate through keys, check if `(target - num)` exists.

  * Special case: if `num == target - num`, need count ≥ 2.

---

## 💻 Java Implementation

```java
class TwoSum {
    private Map<Integer, Integer> table = new HashMap<>();
    
    // Add number to the data structure
    public void add(int number) {
        int count = table.getOrDefault(number, 0);
        table.put(number, count + 1);
    }
    
    // Find if there exists a pair with given sum
    public boolean find(int value) {
        for (Map.Entry<Integer, Integer> entry : table.entrySet()) {
            int num = entry.getKey();
            int y = value - num;
            if (y == num) {
                if (entry.getValue() >= 2) return true;
            } else if (table.containsKey(y)) {
                return true;
            }
        }
        return false;
    }
}
```

---

## 🚀 Python Implementation

```python
class TwoSum:
    def __init__(self):
        self.table = {}
    
    def add(self, number: int) -> None:
        self.table[number] = self.table.get(number, 0) + 1
    
    def find(self, value: int) -> bool:
        for num in self.table:
            y = value - num
            if y == num:
                if self.table[num] >= 2:
                    return True
            elif y in self.table:
                return True
        return False

# Example Usage
ts = TwoSum()
ts.add(1)
ts.add(3)
ts.add(5)
print(ts.find(4))  # True
print(ts.find(7))  # False
```

---

## 🔮 Follow-up

* If `find` is called **very frequently**, prefer **storing all pair sums**.
* If both `add` and `find` are balanced, use **HashMap approach** (best trade-off).
* If input needs to stay **sorted**, use **two pointers**.

---

## ✅ OVERALL SUMMARY – Complexity Checklist

| Approach              | Add Complexity | Find Complexity | Space | Notes                    |
| --------------------- | -------------- | --------------- | ----- | ------------------------ |
| Store Pair Sums       | O(n)           | O(1)            | O(n²) | Best for frequent `find` |
| Sorted + Two Pointers | O(log n)       | O(n)            | O(n)  | Balanced but slower find |
| HashMap (Best)        | O(1)           | O(n)            | O(n)  | Best trade-off ✅         |

```

---

👉 This is **Day 3** in the **exact same format as Day 2** but adapted for *Two Sum III*.  

Do you also want me to prepare **Day 4 (next LeetCode problem)** in advance in this same README style so you just paste and go?
```

---

## 🚀 Python Implementation

```python
class TwoSum:
    def __init__(self):
        self.table = {}
    
    def add(self, number: int) -> None:
        self.table[number] = self.table.get(number, 0) + 1
    
    def find(self, value: int) -> bool:
        for num in self.table:
            y = value - num
            if y == num:
                if self.table[num] >= 2:
                    return True
            elif y in self.table:
                return True
        return False

# Example Usage
ts = TwoSum()
ts.add(1)
ts.add(3)
ts.add(5)
print(ts.find(4))  # True
print(ts.find(7))  # False
```

---

## 🔮 Follow-up

* If `find` is called **very frequently**, prefer **storing all pair sums**.
* If both `add` and `find` are balanced, use **HashMap approach** (best trade-off).
* If input needs to stay **sorted**, use **two pointers**.

---

## ✅ OVERALL SUMMARY – Complexity Checklist

| Approach              | Add Complexity | Find Complexity | Space | Notes                    |
| --------------------- | -------------- | --------------- | ----- | ------------------------ |
| Store Pair Sums       | O(n)           | O(1)            | O(n²) | Best for frequent `find` |
| Sorted + Two Pointers | O(log n)       | O(n)            | O(n)  | Balanced but slower find |
| HashMap (Best)        | O(1)           | O(n)            | O(n)  | Best trade-off ✅         |

```
