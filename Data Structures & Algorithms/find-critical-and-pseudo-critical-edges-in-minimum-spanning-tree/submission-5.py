class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n

    def find(self, v):
        while v != self.par[v]:
            self.par[v] = self.par[self.par[v]]
            v = self.par[v]
        return v

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i)
        edges.sort(key=lambda e: e[2])

        mst_weight = 0
        uf = UnionFind(n)
        for a, b, w, i in edges:
            if uf.union(a, b):
                mst_weight += w

        critical, pseudo = [], []

        for n1, n2, e_weight, i in edges:
            weight = 0
            uf = UnionFind(n)
            for a, b, w, j in edges:
                if i != j and uf.union(a, b):
                    weight += w
            if max(uf.rank) != n or weight > mst_weight:
                critical.append(i)
                continue

            uf = UnionFind(n)
            uf.union(n1, n2)
            weight = e_weight
            for a, b, w, j in edges:
                if uf.union(a, b):
                    weight += w
            if weight == mst_weight:
                pseudo.append(i)

        return [critical, pseudo]

        