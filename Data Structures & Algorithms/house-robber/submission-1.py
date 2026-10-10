class Solution:
    def rob(self, nums: List[int]) -> int:
        # brute force
        def profit(i):
            if i < 0:
                return 0
            profitIncluding = profit(i-2) + nums[i]
            profitWithout = profit(i-1)
            best = max(profitIncluding, profitWithout)
            return best
        
        return profit(len(nums) - 1)