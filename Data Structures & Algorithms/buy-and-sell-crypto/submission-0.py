class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        else:
            current_minimum_price = prices[0]
            current_profit = 0

            for price in prices[1:]:
                profit_candidate = price - current_minimum_price
                if current_profit < profit_candidate:
                    current_profit = profit_candidate
                
                if current_minimum_price > price:
                    current_minimum_price = price
            
            return current_profit
