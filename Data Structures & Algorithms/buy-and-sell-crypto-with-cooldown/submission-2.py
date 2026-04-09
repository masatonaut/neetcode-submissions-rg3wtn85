class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0

        free = 0
        hold = -prices[0]
        wait = float('-inf')

        for i in range(1, len(prices)):
            new_free = max(free, wait)
            new_hold = max(hold, free - prices[i])
            new_wait = hold + prices[i]

            free = new_free
            hold = new_hold
            wait = new_wait

        return max(free, wait)