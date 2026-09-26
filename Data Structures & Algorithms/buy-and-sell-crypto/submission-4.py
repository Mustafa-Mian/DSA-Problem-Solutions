class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = prices[0]
        max_profit = 0

        for price in prices:
            profit = price - best_buy
            max_profit = max(max_profit, profit)
            best_buy = min(price, best_buy)
        return max_profit