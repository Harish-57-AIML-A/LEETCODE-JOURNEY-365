/* The read4 API is defined in the parent class Reader4.
 * int read4(char[] buf4);
 */

public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters actually read
     */
    public int read(char[] buf, int n) {
        char[] buf4 = new char[4];   // Temporary buffer for read4
        int totalRead = 0;           // Total characters copied into buf
        boolean eof = false;         // End of file flag

        while (!eof && totalRead < n) {
            int count = read4(buf4); // Read up to 4 chars
            if (count < 4) {
                eof = true;          // Reached end of file
            }

            // Copy only the required number of characters
            int charsToCopy = Math.min(n - totalRead, count);
            for (int i = 0; i < charsToCopy; i++) {
                buf[totalRead++] = buf4[i];
            }
        }

        return totalRead;  // Return number of chars read
    }
}
