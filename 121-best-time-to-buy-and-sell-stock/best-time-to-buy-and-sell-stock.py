class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        gprofit = 0
        for i in range(len(prices)):
            min_val = min(min_val,prices[i])
            currProfit = prices[i]-min_val
            gprofit = max(gprofit,currProfit)
        return gprofit    
        