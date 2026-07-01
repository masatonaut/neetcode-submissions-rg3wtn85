class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0

        def backtrack(i, current):
            if i == len(nums):
                self.total += current
                return
            current ^= nums[i]
            backtrack(i + 1, current)
            current ^= nums[i]
            backtrack(i + 1, current)

        backtrack(0, 0)
        return self.total