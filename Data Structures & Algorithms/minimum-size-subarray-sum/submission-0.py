class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        result = float('inf')
        for i in range(n):
            for j in range(i, n):
                total = sum(nums[i:j+1])
                if total >= target:
                    result = min(result, j - i + 1)
                    break
        return result if result != float('inf') else 0