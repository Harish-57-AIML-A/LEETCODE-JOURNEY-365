/* The read4 API is defined in the parent class Reader4.
 * int read4(char[] buf);
 */
public class Solution extends Reader4 {
    private char[] buffer = new char[4]; // temp buffer
    private int offset = 0;              // next position in buffer
    private int bufsize = 0;             // number of leftover chars

    /**
     * @param buf Destination buffer
     * @param n   Max number of chars to read
     * @return    Number of chars actually read
     */
    public int read(char[] buf, int n) {
        int readBytes = 0;  // total chars read so far
        boolean eof = false;

        while (!eof && readBytes < n) {
            int sz = (bufsize > 0) ? bufsize : read4(buffer);

            if (bufsize == 0 && sz < 4) {
                eof = true; // reached end of file
            }

            int bytes = Math.min(n - readBytes, sz);
            System.arraycopy(buffer, offset, buf, readBytes, bytes);

            offset = (offset + bytes) % 4;
            bufsize = sz - bytes;
            readBytes += bytes;
        }

        return readBytes;
    }
}
