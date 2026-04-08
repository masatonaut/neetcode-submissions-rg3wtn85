class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0

        buy = 0
        sell = -prices[0]
        cool = float('-inf')

        for i in range(1, len(prices)):
            new_buy  = max(buy, cool)
            new_sell = max(sell, buy - prices[i])
            new_cool = sell + prices[i]
            buy  = new_buy
            sell = new_sell
            cool = new_cool

        return max(buy, cool)