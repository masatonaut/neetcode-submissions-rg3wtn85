class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        free = 0
        hold = -float('inf')

        for price in prices:
            free = max(free, hold + price)
            hold = max(hold, free - price)

        return free