🌟 Day 15 – Read N Characters Given Read4

📌 **Difficulty**: 🟢 Easy

📌 **Frequency**: 📉 N/A

📌 **Link**: 🔗 [LeetCode Problem](https://leetcode.com/problems/read-n-characters-given-read4/)

---

## 📝 Problem Statement

The API:

```java
int read4(char *buf)
```

reads **4 characters at a time** from a file.
The return value = actual number of characters read.

👉 Implement the function:

```java
int read(char *buf, int n)
```

that reads **n characters** from the file using `read4`.

⚠️ **Notes**:

* The `read` function will only be called once per test case.
* If `read4` returns fewer than 4 → it means we’ve reached **end of file** (EOF).
* Even if `read4` returns exactly 4 → it could still be EOF (last 4 chars).

---

## 🔹 Examples

**Example 1**

```text
File = "abcdefghijk", n = 5
read(buf, 5) → "abcde"
```

**Example 2**

```text
File = "xyz", n = 5
read(buf, 5) → "xyz"  (only 3 chars available)
```

---

## 💡 Approach

1. Create a **temporary buffer of size 4** for `read4`.
2. Keep reading chunks of 4 characters until:

   * EOF is reached (`read4` < 4), OR
   * We’ve read `n` characters.
3. Carefully copy only the required number of characters:

   * `min(n - readBytes, sz)` ensures no overflow.
4. Return the **actual number of characters read**.

---

## 🐍 Python Solution (Simulation)

```python
# Mock read4 API for simulation
def read4(buf4: list[str]) -> int:
    global file_data, file_ptr
    cnt = 0
    while cnt < 4 and file_ptr < len(file_data):
        buf4[cnt] = file_data[file_ptr]
        file_ptr += 1
        cnt += 1
    return cnt

def read(buf: list[str], n: int) -> int:
    buffer = [""] * 4
    readBytes = 0
    eof = False
    
    while not eof and readBytes < n:
        sz = read4(buffer)
        if sz < 4:
            eof = True
        bytes_to_copy = min(n - readBytes, sz)
        buf[readBytes:readBytes + bytes_to_copy] = buffer[:bytes_to_copy]
        readBytes += bytes_to_copy
    
    return readBytes


# 🚀 Example Run
file_data, file_ptr = "abcdefghijk", 0
buf = [""] * 20
print(read(buf, 5))   # 5
print("".join(buf[:5]))  # "abcde"
```

---

## ☕ Java Solution

```java
/* The read4 API is defined in the parent class Reader4.
int read4(char[] buf); */

public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n Maximum number of characters to read
     * @return The number of characters read
     */
    public int read(char[] buf, int n) {
        char[] buffer = new char[4];
        int readBytes = 0;
        boolean eof = false;

        while (!eof && readBytes < n) {
            int sz = read4(buffer);
            if (sz < 4) eof = true;

            int bytes = Math.min(n - readBytes, sz);
            System.arraycopy(buffer, 0, buf, readBytes, bytes);
            readBytes += bytes;
        }

        return readBytes;
    }
}
```

---

## 📦 Complexity Analysis

| 🔎 Aspect               | ⚡ Optimized Chunked Read                                                           |
| ----------------------- | ---------------------------------------------------------------------------------- |
| ⏱ **Time Complexity**   | **O(n)** → Each character is processed at most once                                |
| 💾 **Space Complexity** | **O(1)** → Constant extra space (4-char buffer)                                    |
| ✅ **Key Takeaways**     | - Efficient linear scan <br> - Stop at EOF <br> - Careful copy ensures no overflow |

---
