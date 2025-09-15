class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative numbers are not palindromes
        if x < 0:
            return False

        # find divisor to get the leading digit
        div = 1
        while x // div >= 10:
            div *= 10

        while x:
            left = x // div
            right = x % 10
            if left != right:
                return False
            # remove leading and trailing digits
            x = (x % div) // 10
            div //= 100

        return True

# Example runs
sol = Solution()
print(sol.isPalindrome(121))    # True
print(sol.isPalindrome(-121))   # False
print(sol.isPalindrome(10))     # False
print(sol.isPalindrome(12321))  # True
