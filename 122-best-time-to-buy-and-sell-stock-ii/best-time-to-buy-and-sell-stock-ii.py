class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        gprofit = 0
        for i in range(len(prices)):
            min_val = min(min_val, prices[i])
            curr_profit = prices[i]-min_val
            if curr_profit>0:
                min_val = prices[i]
                gprofit +=curr_profit
        return gprofit        
        