public class Solution {
    public int reverse(int x) {
        int result = 0;

        while (x != 0) {
            int digit = x % 10;

            // Check overflow before updating result
            if (result > Integer.MAX_VALUE / 10 || result < Integer.MIN_VALUE / 10) {
                return 0;
            }

            result = result * 10 + digit;
            x /= 10;
        }

        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.reverse(123));     // 321
        System.out.println(sol.reverse(-123));    // -321
        System.out.println(sol.reverse(120));     // 21
        System.out.println(sol.reverse(1000000003)); // 0 (overflow)
    }
}
