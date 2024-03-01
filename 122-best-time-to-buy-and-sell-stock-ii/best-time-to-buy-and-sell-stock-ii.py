class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        gprofit = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            currProfit = prices[i]-min_price
            if currProfit>0:
                min_price = prices[i]
                gprofit += currProfit
        return gprofit        
            
        