public int strStr(String haystack, String needle) {
    for (int i = 0; ; i++) {
        for (int j = 0; ; j++) {
            if (j == needle.length()) return i;       // found match
            if (i + j == haystack.length()) return -1; // reached end
            if (needle.charAt(j) != haystack.charAt(i + j)) break; // mismatch
        }
    }
}
