class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices.copy()
            
            for frm, to, price in flights:
                if prices[frm] == float('inf'):
                    continue

                if prices[frm] + price < temp[to]:
                    temp[to] = prices[frm] + price

            prices = temp

        if prices[dst] == float('inf'):
            return -1

        return prices[dst]