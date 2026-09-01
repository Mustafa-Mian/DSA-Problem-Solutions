def charPos(c):
    return ord(c) - ord('A')

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s) # must be less than 26
        max_len = 0
        for char in charSet: # 26 runs max
            l = 0
            count = 0
            for r in range(len(s)): # O(n)
                cur = s[r]
                if cur == char:
                    count += 1
                    
                window_size = r - l + 1
                replacementsNeeded = window_size - count
                while replacementsNeeded > k:
                    lchar = s[l]
                    if lchar == char:
                        count -= 1
                    l += 1
                    window_size = r - l + 1
                    replacementsNeeded = window_size - count
                
                max_len = max(max_len, window_size)
        return max_len
            