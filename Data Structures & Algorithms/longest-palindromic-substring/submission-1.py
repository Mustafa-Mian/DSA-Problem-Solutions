class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Dynamic programming
        res = ""
        resLen = 0
        n = len(s)
        dp = [[False for i in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if checkPalindrome(i, j, s, dp):
                    if (j - i + 1) > resLen:
                        res = s[i:j+1]
                        resLen = j - i + 1
        return res


def checkPalindrome(i, j, s, dp):
    if (s[i] == s[j]) and (j - i + 1 <= 3 or dp[i+1][j-1]):
        dp[i][j] = True
    return dp[i][j]
