class Solution:
    def climbStairs(self, n: int) -> int:
        # top down memoization dynamic programming buzz words
        dp = {}
        dp[1] = 1
        dp[2] = 2
        return recurseStairs(n, dp)

def recurseStairs(i, dp):
    if i in dp:
        return dp[i]
    else:
        dp[i] = recurseStairs(i-1, dp) + recurseStairs(i-2, dp)
        return dp[i]