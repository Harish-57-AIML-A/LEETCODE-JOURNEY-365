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

