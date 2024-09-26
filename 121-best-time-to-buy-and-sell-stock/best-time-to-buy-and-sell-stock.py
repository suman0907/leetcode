class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        gprofit = 0
        i = 1
        while i<len(prices):
            min_val = min(min_val,prices[i])
            currprofit = prices[i]-min_val
            gprofit = max(gprofit,currprofit)
            i+=1
        return gprofit    
        