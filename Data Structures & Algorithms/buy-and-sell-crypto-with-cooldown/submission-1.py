class Solution:
    # Recursive, times out
    def maxProfit(self, prices: List[int]) -> int:
        def recursePrice(i, buying):
            if i >= len(prices):
                return 0
            myProfit = 0
            skip = recursePrice(i+1, buying)
            if buying:
                myProfit = max(recursePrice(i+1, not buying) - prices[i], skip)
            else:
                myProfit = max(recursePrice(i+2, not buying) + prices[i], skip)
            return myProfit
        return recursePrice(0, True)