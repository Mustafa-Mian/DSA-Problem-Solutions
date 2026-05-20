class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        longestLen = 0
        charsSeen = set()
        l = 0
        
        for r in range(len(s)):
            while s[r] in charsSeen:
                charsSeen.remove(s[l])
                l += 1
            charsSeen.add(s[r])
            longestLen = max(longestLen, r - l + 1)
        return longestLen

