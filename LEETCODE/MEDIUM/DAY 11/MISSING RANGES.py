from typing import List

def findMissingRanges(nums: List[int], start: int, end: int) -> List[str]:
    def get_range(low: int, high: int) -> str:
        return str(low) if low == high else f"{low}->{high}"

    ranges = []
    prev = start - 1
    nums.append(end + 1)  # Add artificial boundary
    
    for curr in nums:
        if curr - prev >= 2:
            ranges.append(get_range(prev + 1, curr - 1))
        prev = curr
    
    return ranges


# 🚀 Example Run
print(findMissingRanges([0, 1, 3, 50, 75], 0, 99))  
# Output: ["2", "4->49", "51->74", "76->99"]

