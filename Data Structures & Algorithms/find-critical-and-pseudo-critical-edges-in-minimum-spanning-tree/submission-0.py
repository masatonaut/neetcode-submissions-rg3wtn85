class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.par[py] = px
        self.rank[px] += self.rank[py]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indexed = [[a, b, w, i] for i, (a, b, w) in enumerate(edges)]
        indexed.sort(key=lambda x: x[2])

        def mst_weight(skip=-1, force=-1):
            uf = UnionFind(n)
            total, count = 0, 0
            if force != -1:
                a, b, w, _ = indexed[force]
                uf.union(a, b); total += w; count += 1
            for j, (a, b, w, _) in enumerate(indexed):
                if j == skip or j == force: continue
                if uf.union(a, b):
                    total += w; count += 1
            return total if count == n - 1 else float('inf')

        base = mst_weight()
        critical, pseudo = [], []

        for j in range(len(indexed)):
            orig_index = indexed[j][3]
            if mst_weight(skip=j) > base:
                critical.append(orig_index)
            elif mst_weight(force=j) == base:
                pseudo.append(orig_index)

        return [critical, pseudo]