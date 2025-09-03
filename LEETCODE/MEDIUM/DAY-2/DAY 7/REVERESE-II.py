def reverseWords(s: list) -> None:
    def reverse(l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1

    # Step 1: Reverse entire string
    reverse(0, len(s) - 1)

    # Step 2: Reverse each word
    i = 0
    for j in range(len(s) + 1):
        if j == len(s) or s[j] == ' ':
            reverse(i, j - 1)
            i = j + 1

# Example Usage
chars = list("the sky is blue")
reverseWords(chars)
print("".join(chars))  # "blue is sky the"

