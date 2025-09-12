🌟 Day 16 – Read N Characters Given Read4 (Multiple Calls)

📌 **Difficulty**: 🔴 Hard

📌 **Frequency**: 📉 N/A

📌 **Link**: [🔗 LeetCode Problem](https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/)

---

## 📝 Problem Statement

The API:

```java
int read4(char[] buf);
```

📌 **Reads 4 characters at a time from a file.**

* Returns the **number of characters actually read**.
* If fewer than 4, it means EOF (End Of File).

---

### 🔹 Task

Implement the function:

```java
int read(char[] buf, int n)
```

* Reads **up to n characters** from the file.
* Unlike Day 15, here **`read` can be called multiple times**.

---

## ⚡ Challenges

* Must **store leftover data** between multiple calls.
* Need **persistent state variables**:

  1. **buffer\[4]** → Temp buffer for data from `read4`.
  2. **offset** → Next position in `buffer` to read from.
  3. **bufsize** → Number of leftover chars in buffer.

---

## 💡 Approach

1. **Check leftover buffer** → If `bufsize > 0`, consume it before calling `read4`.
2. **Read new data** using `read4` if no leftovers.
3. Copy characters from `buffer` into `buf`.
4. Adjust `offset` and `bufsize` after copying.
5. Repeat until either:

   * Reached `n` characters, OR
   * EOF is encountered.

---

## ☕ Java Solution

```java
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
```

---

## 🐍 Python (Conceptual Simulation)

⚠️ Python does not have `read4` built-in. Below is a **simulated version**.

```python
# Simulated API
def read4(buf4):
    global file_data, file_ptr
    count = 0
    while count < 4 and file_ptr < len(file_data):
        buf4[count] = file_data[file_ptr]
        file_ptr += 1
        count += 1
    return count

class Reader:
    def __init__(self):
        self.buffer = [""] * 4
        self.offset = 0
        self.bufsize = 0

    def read(self, buf, n):
        readBytes = 0
        eof = False

        while not eof and readBytes < n:
            sz = self.bufsize if self.bufsize > 0 else read4(self.buffer)

            if self.bufsize == 0 and sz < 4:
                eof = True

            bytes_to_copy = min(n - readBytes, sz)
            for i in range(bytes_to_copy):
                buf.append(self.buffer[self.offset + i])

            self.offset = (self.offset + bytes_to_copy) % 4
            self.bufsize = sz - bytes_to_copy
            readBytes += bytes_to_copy

        return readBytes
```

---

## 📊 Complexity Analysis

| 🔎 Aspect               | ⚡ Optimized Approach                            |
| ----------------------- | ----------------------------------------------- |
| ⏱ **Time Complexity**   | `O(n)` → Each character read once               |
| 💾 **Space Complexity** | `O(1)` → Only constant extra buffer (`4 chars`) |
| 🔁 **Multiple Calls**   | ✅ Maintains leftover state across calls         |

---

## ✅ Key Takeaways

* Day 16 is an **extension of Day 15** with **state persistence**.
* **offset + bufsize trick** handles leftovers seamlessly.
* 🚫 Don’t re-read discarded characters → store them for the next call.
* ⚡ Ensures correctness in **multi-call scenarios**.

---


