import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        heap = [(0, 0, 0)]
        visited = set()

        while heap:
            effort, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == rows - 1 and c == cols - 1:
                return effort

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    diff = abs(heights[nr][nc] - heights[r][c])
                    new_effort = max(effort, diff)
                    heapq.heappush(heap, (new_effort, nr, nc))

        return 0