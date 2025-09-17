def twoSum(numbers, target):
    num_map = {}  # dictionary to store value -> index
    for i, x in enumerate(numbers):
        complement = target - x
        if complement in num_map:
            return [num_map[complement] + 1, i + 1]  # +1 for 1-based indexing
        num_map[x] = i
    raise ValueError("No two sum solution")

