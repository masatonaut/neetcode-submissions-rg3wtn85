class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            result = max(result, curr)

        return result