class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            tmp_max = max(nums[i], nums[i] * curr_max, nums[i] * curr_min)
            tmp_min = min(nums[i], nums[i] * curr_max, nums[i] * curr_min)

            curr_max = tmp_max
            curr_min = tmp_min
            result = max(result, curr_max)

        return result