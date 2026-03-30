class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit = set()

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        count = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                count += 1

        return count