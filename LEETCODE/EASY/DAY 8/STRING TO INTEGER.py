def myAtoi(s: str) -> int:
    s = s.lstrip()  # remove leading whitespaces
    if not s:
        return 0
    
    # Handle sign
    sign = 1
    if s[0] in ['-', '+']:
        if s[0] == '-':
            sign = -1
        s = s[1:]
    
    # Convert digits
    num = 0
    for char in s:
        if not char.isdigit():
            break
        digit = int(char)
        
        # Handle overflow
        if num > (2**31 - 1) // 10 or (num == (2**31 - 1) // 10 and digit > 7):
            return (2**31 - 1) if sign == 1 else -(2**31)
        
        num = num * 10 + digit
    
    return sign * num

# Example Usage
print(myAtoi("   -42"))  # -42
