class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for i in range(len(prices)):
            min_price = min(min_price,prices[i])
            curr_profit = prices[i]-min_price
            profit = max(profit,curr_profit)
        return profit    

        