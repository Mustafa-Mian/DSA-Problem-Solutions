class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Recursive without DP
        n = len(cost)
        def recurseCost(i):
            if i >= n:
                return 0
            myCost = cost[i] + min(recurseCost(i+1), recurseCost(i+2))
            return myCost
        return min(recurseCost(1), recurseCost(0))
