class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute force
        longestLen = 0
        for i in range(len(s)):
            charsSeen = set()
            for j in range(i, len(s)):
                if s[j] in charsSeen:
                    break
                charsSeen.add(s[j])
                longestLen = max(longestLen, len(charsSeen))
        return longestLen
