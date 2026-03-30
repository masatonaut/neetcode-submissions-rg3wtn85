class Solution:
    def rob(self, nums: List[int]) -> int:
        next1, next2 = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            curr = max(nums[i] + next2, next1)
            next2 = next1
            next1 = curr

        return next1