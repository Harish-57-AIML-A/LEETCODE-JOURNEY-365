def reverseWords(s: str) -> str:
    words = s.strip().split()
    return " ".join(reversed(words))

# Example Usage
print(reverseWords("  the sky   is blue "))  # "blue is sky the"
print(reverseWords("hello world"))           # "world hello"

