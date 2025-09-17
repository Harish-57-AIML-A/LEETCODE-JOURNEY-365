def isOneEditDistance(s: str, t: str) -> bool:
    m, n = len(s), len(t)
    if m > n:
        return isOneEditDistance(t, s)
    if n - m > 1:
        return False

    i = 0
    while i < m and s[i] == t[i]:
        i += 1

    if i == m:
        return n - m == 1  # Extra char at end

    if m == n:
        i += 1  # Skip one mismatch

    while i < m and s[i] == t[i + (n - m)]:
        i += 1

    return i == m


# 🚀 Example Run
print(isOneEditDistance("ab", "acb"))   # True
print(isOneEditDistance("cab", "ad"))   # False
print(isOneEditDistance("1203", "1213")) # True

