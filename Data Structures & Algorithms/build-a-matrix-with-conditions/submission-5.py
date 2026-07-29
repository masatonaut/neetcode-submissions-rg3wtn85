from collections import deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(conditions, k):
            adj = {i : [] for i in range(1, k+1)}
            indeg = {i: 0 for i in range(1, k+1)}

            for u, v in conditions:
                adj[u].append(v)
                indeg[v] += 1

            q = deque([i for i in range(1, k+1) if indeg[i] == 0])
            order = []

            while q:
                node = q.popleft()
                order.append(node)
                for nei in adj[node]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        q.append(nei)

            return order if len(order) == k else []

        row_order = topo_sort(rowConditions, k)
        col_order = topo_sort(colConditions, k)

        if not row_order or not col_order:
            return []

        row_index = {num: i for i, num in enumerate(row_order)}
        col_index = {num: i for i, num in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k+1):
            matrix[row_index[num]][col_index[num]] = num

        return matrix