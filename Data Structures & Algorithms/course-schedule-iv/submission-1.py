class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        from collections import defaultdict

        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(start):
            reachable = set()
            def visit(node):
                for nei in graph[node]:
                    if nei not in reachable:
                        reachable.add(nei)
                        visit(nei)
            visit(start)
            return reachable

        reach_map = {}
        for i in range(numCourses):
            reach_map[i] = dfs(i)

        return [v in reach_map[u] for u, v in queries]