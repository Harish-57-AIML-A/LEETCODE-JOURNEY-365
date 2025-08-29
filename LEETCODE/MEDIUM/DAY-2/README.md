📌 Problem 2: Two Sum II – Input Array Is Sorted

🔗 LeetCode Link: Two Sum II

📊 Difficulty: Medium
🔥 Frequency: High

📝 Problem Statement

Given a 1-indexed sorted array of integers numbers, return the indices of the two numbers such that they add up to a specific target number.

Each input has exactly one solution.

You may not use the same element twice.

Indices must be returned in ascending order.

📖 Example

Input:

numbers = [2, 7, 11, 15], target = 9


Output:

[1, 2]

⚙️ Approaches
1. Binary Search – O(n log n) runtime, O(1) space

For each element x, search for target - x using binary search.

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

2. Two Pointers – O(n) runtime, O(1) space ✅ (Best Solution)

Since the array is sorted, we can use two pointers:

If the sum is too large → move j left.

If the sum is too small → move i right.

If equal → found solution.

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

🚀 Python Implementation
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

✅ OVERALL SUMMARY - COMPLEXITY COMPARISON

Binary Search: O(n log n), doesn’t fully use sorted property.

Two Pointers: O(n), O(1) space → Best for sorted input.
