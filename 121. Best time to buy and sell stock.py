class Solution:
    def maxProfit(self, prices):
        lowest = prices[0]
        profit = 0

        for price in prices:
            if price < lowest:
                lowest = price
            else:
                current_profit = price - lowest

                if current_profit > profit:
                    profit = current_profit

        return profit
