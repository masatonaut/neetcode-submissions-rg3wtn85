class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                left, right = b + 1, n - 1
                while left < right:
                    total = nums[a] + nums[b] + nums[left] + nums[right]

                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[a], nums[b], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return result