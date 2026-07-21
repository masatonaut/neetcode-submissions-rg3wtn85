from functools import lru_cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        @lru_cache(maxsize=None)
        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0

            result = dfs(i + 1, j)
            if s[i] == t[j]:
                result += dfs(i + 1, j + 1)
            return result

        return dfs(0, 0)