class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        order = sorted(range(m), key=lambda i: edges[i][2])

        def mst(skip, force):
            par = list(range(n))

            def find(x):
                while x != par[x]:
                    par[x] = par[par[x]]
                    x = par[x]
                return x

            total = cnt = 0

            if force >= 0:
                a, b, w = edges[force]
                par[find(a)] = find(b)
                total, cnt = w, 1

            for i in order:
                if i == skip or i == force:
                    continue
                a, b, w = edges[i]
                ra, rb = find(a), find(b)
                if ra != rb:
                    par[ra] = rb
                    total += w
                    cnt += 1

            return total if cnt == n - 1 else float('inf')

        base = mst(-1, -1)
        crit, pseudo = [], []
        for i in range(m):
            if mst(i, -1) > base:
                crit.append(i)
            elif mst(-1, i) == base:
                pseudo.append(i)
        return [crit, pseudo]