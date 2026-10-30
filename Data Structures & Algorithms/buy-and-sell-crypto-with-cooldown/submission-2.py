class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # top down dp
        dp = {}
        def recursePrice(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            skip = recursePrice(i+1, buying)
            if buying:
                dp[(i, buying)] = max(recursePrice(i+1, not buying) - prices[i], skip)
            else:
                dp[(i, buying)] = max(recursePrice(i+2, not buying) + prices[i], skip)
            return dp[(i, buying)]
        return recursePrice(0, True)