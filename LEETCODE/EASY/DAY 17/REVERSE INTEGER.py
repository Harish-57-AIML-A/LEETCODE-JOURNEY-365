class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check overflow before adding
            if result > (2**31 - 1) // 10:
                return 0

            result = result * 10 + digit

        return sign * result


# 🚀 Example Run
sol = Solution()
print(sol.reverse(123))       # 321
print(sol.reverse(-123))      # -321
print(sol.reverse(120))       # 21
print(sol.reverse(1000000003)) # 0 (overflow)
