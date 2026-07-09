from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def bfs(start, target):
            if start not in graph or target not in graph:
                return -1.0
            queue = deque([(start, 1.0)])
            visited = {start}
            while queue:
                cur, product = queue.popleft()
                if cur == target:
                    return product
                for nei, val in graph[cur].items():
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, product * val))
            return -1.0

        return [bfs(c, d) for c, d in queries]

        def bfs(start, target):
            if start not in graph or target not in graph:
                return -1.0

            queue = deque([(start, 1.0)])