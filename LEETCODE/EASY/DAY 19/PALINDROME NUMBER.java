public class Solution {
    public boolean isPalindrome(int x) {
        // Negative numbers are not palindromes
        if (x < 0) return false;

        // Find the divisor to extract the leading digit
        int div = 1;
        while (x / div >= 10) {
            // watch out for overflow of div (but div stays <= 1e9 for 32-bit int)
            div *= 10;
        }

        while (x != 0) {
            int left = x / div;      // leading digit
            int right = x % 10;      // trailing digit
            if (left != right) return false;

            // remove leading and trailing digits
            x = (x % div) / 10;
            // removed two digits, so reduce divisor by factor 100
            div /= 100;
        }

        return true;
    }

    // quick tests
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.isPalindrome(121));    // true
        System.out.println(s.isPalindrome(-121));   // false
        System.out.println(s.isPalindrome(10));     // false
        System.out.println(s.isPalindrome(12321));  // true
    }
}
