---

````markdown
# 🚀 LeetCode Daily – Day 3

## 📌 Problem: Two Sum III – Data Structure Design  
**Difficulty:** Easy  
**Topic:** Hashing / Two Pointers / Data Structure Design  

---

### 📝 Problem Statement  
Design and implement a `TwoSum` class that supports two operations:  

- **add(input)** → Add the number `input` to an internal data structure.  
- **find(value)** → Find if there exists any pair of numbers which sum is equal to the `value`.  

**Example:**  
```text
add(1); add(3); add(5);
find(4) → true
find(7) → false
````

---

### 💡 Approaches

#### ✅ Approach 1 – Store Pair Sums in Hash Table

* **add**: O(n)
* **find**: O(1)
* **Space**: O(n²)

Good when **find operations are more frequent** than add operations.

---

#### ✅ Approach 2 – Maintain Sorted Array + Two Pointers

* **add**: O(log n) (using binary search insert)
* **find**: O(n)
* **Space**: O(n)

Useful when **data needs to stay sorted**.

---

#### ✅ Approach 3 – HashMap (Efficient & Simple)

* **add**: O(1)
* **find**: O(n)
* **Space**: O(n)

Best trade-off for most cases.

---

### 🧑‍💻 Code Implementation (Java)

```java
import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    private Map<Integer, Integer> table = new HashMap<>();

    // Add number into the data structure
    public void add(int input) {
        int count = table.getOrDefault(input, 0);
        table.put(input, count + 1);
    }

    // Find if there exists a pair with the given sum
    public boolean find(int val) {
        for (Map.Entry<Integer, Integer> entry : table.entrySet()) {
            int num = entry.getKey();
            int complement = val - num;

            if (complement == num) {
                if (entry.getValue() >= 2) return true; // Handle duplicates
            } else if (table.containsKey(complement)) {
                return true;
            }
        }
        return false;
    }
}
```

---

### 🔍 Example Run

```java
TwoSum obj = new TwoSum();
obj.add(1);
obj.add(3);
obj.add(5);

System.out.println(obj.find(4)); // true
System.out.println(obj.find(7)); // false
```

---

### 📊 Complexity Analysis

* **Time Complexity:**

  * `add()` → O(1)
  * `find()` → O(n)

* **Space Complexity:** O(n)

---

### 🏆 Key Takeaways

* This problem teaches **data structure design** with trade-offs between **time** and **space**.
* Using **HashMap** is the most practical approach.
* Useful for problems requiring **frequent add + occasional search**.

---
