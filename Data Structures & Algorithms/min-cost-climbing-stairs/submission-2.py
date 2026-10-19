class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top down DP
        n = len(cost)
        dp = {}
        dp[n] = 0
        def recurseCost(i):
            if i in dp:
                return dp[i]
            if i >= n:
                return dp[n]
            dp[i] = cost[i] + min(recurseCost(i+1), recurseCost(i+2))
            return dp[i]
        return min(recurseCost(1), recurseCost(0))
