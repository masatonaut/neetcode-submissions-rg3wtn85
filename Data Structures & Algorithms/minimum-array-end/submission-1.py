class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x
        remaining = n - 1
        k = 0

        while remaining:
            if (x >> k) & 1 == 0:
                if remaining & 1:
                    result |= (1 << k)
                remaining >>= 1
            k += 1

        return result