class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()
        l = 0
        r = 0
        maxL = 0

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            windowLen = len(seen)
            maxL = max(maxL, windowLen)
            r += 1
        
        return maxL