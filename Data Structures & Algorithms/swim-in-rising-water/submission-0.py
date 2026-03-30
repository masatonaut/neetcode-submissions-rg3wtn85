class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        heap = [(grid[0][0], 0, 0)]
        visit = set()
        visit.add((0, 0))

        while heap:
            max_height, r, c = heapq.heappop(heap)

            if r == n - 1 and c == n - 1:
                return max_height

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    new_max = max(max_height, grid[nr][nc])
                    heapq.heappush(heap, (new_max, nr, nc))

        return -1