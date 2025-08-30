````markdown
🚀 Day 3 – Two Sum III: Data Structure Design

📌 Problem Statement  
Design and implement a `TwoSum` class. It should support the following operations:  

- **add(input)** → Add the number `input` to an internal data structure.  
- **find(value)** → Find if there exists any pair of numbers such that their sum equals `value`.  

Example
```java
add(1);
add(3);
add(5);
find(4) → true   // because 1 + 3 = 4
find(7) → false  // no two numbers sum to 7
````

---

## 💡 Approaches

### 1️⃣ Hash Table with Pair Sums

* **add:** O(n) → compute all pair sums for each new number.
* **find:** O(1) → direct lookup in hash table.
* **Space:** O(n²).
* ✅ Best when `find` operations >> `add` operations.

---

### 2️⃣ Sorted Array + Two Pointers

* Maintain a sorted array.
* **add:** O(log n) (binary search insert).
* **find:** O(n) (two pointer sum search).
* **Space:** O(n).

---

### 3️⃣ Hash Table (Store Counts) – Efficient & Simple

* Store numbers in a **HashMap** with their frequency.
* **add:** O(1).
* **find:** O(n) (iterate through keys and check complement).
* **Space:** O(n).
* ✅ Practical and balanced approach.

---

## 🧑‍💻 Code Implementation (Java)

```java
import java.util.*;

public class TwoSum {
    private Map<Integer, Integer> table = new HashMap<>();

    // Add number to the structure
    public void add(int input) {
        int count = table.getOrDefault(input, 0);
        table.put(input, count + 1);
    }

    // Check if a pair exists
    public boolean find(int val) {
        for (Map.Entry<Integer, Integer> entry : table.entrySet()) {
            int num = entry.getKey();
            int complement = val - num;

            if (complement == num) {
                // Need at least two instances
                if (entry.getValue() >= 2) return true;
            } else if (table.containsKey(complement)) {
                return true;
            }
        }
        return false;
    }

    // Demo run
    public static void main(String[] args) {
        TwoSum ts = new TwoSum();
        ts.add(1);
        ts.add(3);
        ts.add(5);

        System.out.println(ts.find(4)); // true
        System.out.println(ts.find(7)); // false
    }
}
```

---

## ⏱ Complexity Analysis

* **Time:**

  * `add`: O(1)
  * `find`: O(n)
* **Space:** O(n)

---

## ✅ Key Takeaways

* Trade-offs exist between **fast add vs fast find**.
* The **HashMap approach** is the most practical choice.
* Handling **duplicates** correctly is crucial.

```

---

Do you want me to also create the **Day 3 README with the same emojis, bold styling, and section titles** as your **Day 2 README** (like a daily log), so it feels like part of a continuous 30-day challenge?
```
