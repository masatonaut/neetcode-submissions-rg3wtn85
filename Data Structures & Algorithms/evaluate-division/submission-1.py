from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def dfs(cur, target, product, visited):
            if cur not in graph:
                return -1.0
            if cur == target:
                return product
            visited.add(cur)
            for nei, val in graph[cur].items():
                if nei not in visited:
                    result = dfs(nei, target, product * val, visited)
                    if result != -1.0:
                        return result
            return -1.0

        return [dfs(c, d, 1.0, set()) for c, d in queries]