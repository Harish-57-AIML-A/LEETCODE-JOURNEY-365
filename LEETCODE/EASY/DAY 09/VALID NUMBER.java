public class Solution {
    public boolean isNumber(String s) {
        int i = 0, n = s.length();

        // Step 1: Skip leading whitespaces
        while (i < n && Character.isWhitespace(s.charAt(i))) i++;

        // Step 2: Optional sign
        if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) i++;

        boolean isNumeric = false;

        // Step 3: Integer part
        while (i < n && Character.isDigit(s.charAt(i))) {
            i++;
            isNumeric = true;
        }

        // Step 4: Decimal part
        if (i < n && s.charAt(i) == '.') {
            i++;
            while (i < n && Character.isDigit(s.charAt(i))) {
                i++;
                isNumeric = true;
            }
        }

        // Step 5: Skip trailing whitespaces
        while (i < n && Character.isWhitespace(s.charAt(i))) i++;

        return isNumeric && i == n;
    }
}
