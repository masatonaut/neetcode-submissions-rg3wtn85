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
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if 1 in nums:
            return False

        MAX = max(nums)

        spf = list(range(MAX + 1))
        d = 2
        while d * d <= MAX:
            if spf[d] == d:
                for m in range(d * d, MAX + 1, d):
                    if spf[m] == m:
                        spf[m] = d

            d += 1

        uf = UnionFind(n)
        prime_to_idx = {}

        for i, num in enumerate(nums):
            while num > 1:
                p = spf[num]
                if p in prime_to_idx:
                    uf.union(i, prime_to_idx[p])
                else:
                    prime_to_idx[p] = i
                while num % p == 0:
                    num //= p

        return max(uf.rank) == n