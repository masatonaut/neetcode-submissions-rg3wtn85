class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_capital = [(capital[i], profits[i]) for i in range(len(profits))]
        heapq.heapify(min_capital)

        max_profit = []

        for _ in range(k):
            while min_capital and min_capital[0][0] <= w:
                cap, prof = heapq.heappop(min_capital)
                heapq.heappush(max_profit, -prof)

            if not max_profit:
                break

            w += -heapq.heappop(max_profit)

        return w