class Solution:
    def isNumber(self, s: str) -> bool:
        i, n = 0, len(s)

        # Step 1: Skip leading whitespaces
        while i < n and s[i].isspace():
            i += 1

        # Step 2: Optional sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            i += 1

        is_numeric = False

        # Step 3: Integer part
        while i < n and s[i].isdigit():
            i += 1
            is_numeric = True

        # Step 4: Decimal part
        if i < n and s[i] == '.':
            i += 1
            while i < n and s[i].isdigit():
                i += 1
                is_numeric = True

        # Step 5: Skip trailing whitespaces
        while i < n and s[i].isspace():
            i += 1

        return is_numeric and i == n
