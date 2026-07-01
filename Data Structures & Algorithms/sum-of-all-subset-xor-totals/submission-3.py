class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0

        def backtrack(start, current):
            self.total += current
            for i in range(start, len(nums)):
                backtrack(i + 1, current ^ nums[i])

        backtrack(0, 0)
        return self.total