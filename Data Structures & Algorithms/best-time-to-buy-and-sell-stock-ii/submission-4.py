class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        free = 0
        hold = -float('inf')

        for price in prices:
            prev_free, prev_hold = free, hold
            free = max(prev_free, prev_hold + price)
            hold = max(prev_hold, prev_free - price)
        return free