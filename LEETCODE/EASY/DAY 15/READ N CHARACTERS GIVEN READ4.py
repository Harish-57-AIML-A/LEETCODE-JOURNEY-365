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
