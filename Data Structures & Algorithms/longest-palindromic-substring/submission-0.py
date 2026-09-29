class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute force, works but fails time limit
        result = ""
        longestLen = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if checkPalindrome(i, j, s):
                    if (j - i + 1) > longestLen:
                        result = s[i:j+1]
                        longestLen = (j - i + 1)
        return result

def checkPalindrome(i, j, s):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
