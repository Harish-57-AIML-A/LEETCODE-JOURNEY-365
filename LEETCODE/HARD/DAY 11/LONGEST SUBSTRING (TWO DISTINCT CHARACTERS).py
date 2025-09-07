def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    from collections import defaultdict
    
    count = defaultdict(int)
    i = 0
    max_len = 0
    
    for j, ch in enumerate(s):
        count[ch] += 1
        
        while len(count) > 2:
            count[s[i]] -= 1
            if count[s[i]] == 0:
                del count[s[i]]
            i += 1
        
        max_len = max(max_len, j - i + 1)
    
    return max_len


# 🚀 Example Run
print(lengthOfLongestSubstringTwoDistinct("eceba"))   # Output: 3
print(lengthOfLongestSubstringTwoDistinct("ccaabbb")) # Output: 5
