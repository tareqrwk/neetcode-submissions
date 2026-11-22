class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        best_profit = 0 
        for i in range(len(prices)):
            profit = prices[i] - lowest_price
            best_profit = max(profit, best_profit)
            if prices[i] < lowest_price:
                lowest_price = prices[i]
        return best_profit
        