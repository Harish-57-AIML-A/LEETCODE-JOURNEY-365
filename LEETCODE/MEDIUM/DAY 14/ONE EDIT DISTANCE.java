class Solution {
    public boolean isOneEditDistance(String s, String t) {
        int m = s.length(), n = t.length();
        if (m > n) return isOneEditDistance(t, s);
        if (n - m > 1) return false;

        int i = 0;
        while (i < m && s.charAt(i) == t.charAt(i)) i++;

        if (i == m) return n - m == 1; // Extra char at end

        if (m == n) i++; // Modification case

        while (i < m && s.charAt(i) == t.charAt(i + (n - m))) i++;

        return i == m;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isOneEditDistance("ab", "acb"));   // true
        System.out.println(sol.isOneEditDistance("cab", "ad"));   // false
        System.out.println(sol.isOneEditDistance("1203", "1213")); // true
    }
}

