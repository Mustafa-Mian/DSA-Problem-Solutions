class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = prices[0]
        max_profit = 0

        for price in prices:
            profit = price - best_buy
            if profit > max_profit:
                max_profit = profit
            if price < best_buy:
                best_buy = price
        
        return max_profit