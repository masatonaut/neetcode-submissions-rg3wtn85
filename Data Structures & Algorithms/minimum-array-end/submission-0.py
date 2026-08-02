class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x
        remaining = n - 1
        bit = 0

        while remaining:
            if (x >> bit) & 1 == 0:
                if remaining & 1:
                    result |= (1 << bit)
                remaining >>= 1
            bit += 1

        return result