class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        def splits_needed(target):
            splits = 1
            current = 0
            for n in nums:
                if current + n > target:
                    splits += 1
                    current = n
                else:
                    current += n

            return splits

        while left < right:
            mid = (left + right) // 2
            if splits_needed(mid) <= k:
                right = mid
            else:
                left = mid + 1

        return left