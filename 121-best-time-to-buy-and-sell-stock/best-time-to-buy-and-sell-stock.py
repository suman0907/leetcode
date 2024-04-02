class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        g_profit = 0
        min_val = prices[0]
        for i in range(len(prices)):
            min_val = min(min_val,prices[i])
            curr_profit = prices[i]-min_val
            g_profit = max(g_profit,curr_profit)
        return g_profit    
        