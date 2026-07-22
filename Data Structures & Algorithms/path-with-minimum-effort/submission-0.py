import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        heap = [(0, 0, 0)]
        visited = set()

        while heap:
            effort, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue
            if r == rows - 1 and c == cols - 1:
                return effort
            visited.add((r, c))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    diff = abs(heights[nr][nc] - heights[r][c])
                    new_effort = max(effort, diff)
                    heapq.heappush(heap, (new_effort, nr, nc))

        return 0