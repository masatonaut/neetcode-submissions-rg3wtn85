class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n

    def find(self, v):
        if v != self.par[v]:
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

        uf = UnionFind(n)
        prime_owner = {}

        for i, num in enumerate(nums):
            if nums == 1:
                return False

            primes = []
            x = num
            d = 2
            while d * d <= x:
                if x % d == 0:
                    primes.append(d)
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                primes.append(x)

            for p in primes:
                if p in prime_owner:
                    uf.union(i, prime_owner[p])
                else:
                    prime_owner[p] = i

        return max(uf.rank) == n