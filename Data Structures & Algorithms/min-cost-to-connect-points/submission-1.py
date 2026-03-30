class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def distance(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        visit = set()
        heap = [(0, 0)]
        total_cost = 0

        while len(visit) < n:
            cost, node = heapq.heappop(heap)

            if node in visit:
                continue

            visit.add(node)
            total_cost += cost

            for next_node in range(n):
                if next_node not in visit:
                    heapq.heappush(heap, (distance(next_node, node), next_node))

        return total_cost