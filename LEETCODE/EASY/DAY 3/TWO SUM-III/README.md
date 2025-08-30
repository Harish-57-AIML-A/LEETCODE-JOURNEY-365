📌 Problem 3: Two Sum III – Data Structure Design

🔗 LeetCode Link: Two Sum III – Data Structure Design

📊 Difficulty: Easy
🔥 Frequency: Medium

📝 Problem Statement

Design and implement a TwoSum class that supports the following operations:

add(input) → Add the number to an internal data structure.

find(value) → Check if there exists any pair of numbers which sum equals the value.

📖 Example

Input / Output Flow:

TwoSum ts = new TwoSum();
ts.add(1);
ts.add(3);
ts.add(5);

System.out.println(ts.find(4)); // true  (1 + 3)
System.out.println(ts.find(7)); // false (no such pair)

⚙️ Approaches
1️⃣ Store All Pair Sums

Add: O(n)

Find: O(1) ✅

Space: O(n²)

Idea: Precompute all pair sums and store them in a hash set.

Works best when find() is called much more frequently than add().

2️⃣ Sorted Array + Two Pointers

Add: O(log n) (insert with binary search)

Find: O(n)

Space: O(n)

Keep numbers sorted, then use two pointers for searching.

3️⃣ HashMap with Counts (Best Tradeoff) ✅

Add: O(1)

Find: O(n)

Space: O(n)

Store each number in a hash map with frequency.

For each key, check if target - key exists.

Special handling for duplicates (e.g., [2, 2] when target = 4).

🧩 Java Implementation
import java.util.*;

public class TwoSum {
    private Map<Integer, Integer> table = new HashMap<>();

    // Add number to structure
    public void add(int input) {
        table.put(input, table.getOrDefault(input, 0) + 1);
    }

    // Find if pair exists
    public boolean find(int val) {
        for (Map.Entry<Integer, Integer> entry : table.entrySet()) {
            int num = entry.getKey();
            int target = val - num;

            if (target == num) {
                // Need at least 2 duplicates
                if (entry.getValue() >= 2) return true;
            } else if (table.containsKey(target)) {
                return true;
            }
        }
        return false;
    }

    // Example usage
    public static void main(String[] args) {
        TwoSum ts = new TwoSum();
        ts.add(1);
        ts.add(3);
        ts.add(5);

        System.out.println(ts.find(4)); // true
        System.out.println(ts.find(7)); // false
    }
}

🚀 Python Implementation
class TwoSum:
    def __init__(self):
        self.table = {}

    def add(self, number: int) -> None:
        self.table[number] = self.table.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for num in self.table:
            target = value - num
            if target == num:
                if self.table[num] >= 2:
                    return True
            elif target in self.table:
                return True
        return False

# Example usage
ts = TwoSum()
ts.add(1)
ts.add(3)
ts.add(5)
print(ts.find(4))  # True
print(ts.find(7))  # False

📊 Complexity Summary
Approach	Add Time	Find Time	Space	Notes
Store Pair Sums	O(n)	O(1)	O(n²)	Best when find() >> add()
Sorted Array + Two Pointers	O(log n)	O(n)	O(n)	Balanced but slower add
HashMap with Counts ✅	O(1)	O(n)	O(n)	Best practical choice
🎯 Takeaway

The HashMap with counts approach offers the best balance between fast add() and efficient find().
