class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two ptrs / sliding window
        max_profit = 0
        l = 0
        r = 1
        while r < (len(prices)):
            if prices[r] > prices[l]:
                cur_profit = prices[r] - prices[l]
                max_profit = max(max_profit, cur_profit)
                r += 1
            else:
                l = r
                r = l + 1
        return max_profit