class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp top down
        dp = {}
        def profit(i):
            if i < 0:
                return 0
            if i in dp:
                return dp[i]
            profitIncluding = profit(i-2) + nums[i]
            profitWithout = profit(i-1)
            best = max(profitIncluding, profitWithout)
            dp[i] = best
            return best
        
        return profit(len(nums) - 1)