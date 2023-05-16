class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        profit = 0
        for i in range(len(prices)):
            min_p = min(min_p,prices[i])
            curr_p = prices[i]-min_p
            profit = max(profit,curr_p)
        return profit    

