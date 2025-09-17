def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
        else:
            return i
    return -1

# Example Usage
print(strStr("hello", "ll"))  # 2
print(strStr("aaaaa", "bba"))  # -1

