class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        
        while r < len(prices):
            # it checks if it makes sense to buy a stock
            # reminder: we  want to  buy cheap and sell expensive
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            # in case when it's not profitable we wanna shift left pointer to the right
            else:
                l = r
                
            r += 1
            
        return max_profit
