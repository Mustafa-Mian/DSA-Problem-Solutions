class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for i in range(n+1, -1, -1):
            for j in range(i, n):
                if isPalindrome(i, j, s, dp):
                    count += 1
        return count

def isPalindrome(i, j, s, dp):
    if s[i] == s[j] and (j - i + 1 <= 3 or dp[i+1][j-1]):
        dp[i][j] = True
    return dp[i][j]