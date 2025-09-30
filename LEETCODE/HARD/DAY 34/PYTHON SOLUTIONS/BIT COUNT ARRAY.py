class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = [0] * 32
        result = 0
        for i in range(32):
            for num in nums:
                if (num >> i) & 1:
                    count[i] += 1
            result |= (count[i] % 3) << i
        # Handle negative numbers
        if result >= 2**31:
            result -= 2**32
        return result
