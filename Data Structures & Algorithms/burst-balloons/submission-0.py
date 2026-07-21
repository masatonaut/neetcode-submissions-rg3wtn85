from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums) - 2

        @lru_cache(maxsize=None)
        def dp(l, r):
            if l > r:
                return 0
            best = 0
            for i in range(l, r + 1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                total = dp(l, i-1) + coins + dp(i+1, r)
                best = max(best, total)
            return best

        return dp(1, n)