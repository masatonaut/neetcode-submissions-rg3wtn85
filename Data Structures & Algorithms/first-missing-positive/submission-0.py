class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        n = len(nums)
        for i in range(1, n + 2):
            if i not in s:
                return i