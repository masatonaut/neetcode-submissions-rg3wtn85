class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(i, current):
            if i == len(nums):
                return current

            include = backtrack(i + 1, current ^ nums[i])
            exclude = backtrack(i + 1, current)

            return include + exclude

        return backtrack(0, 0)