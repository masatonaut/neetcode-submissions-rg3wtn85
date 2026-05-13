class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self._quicksort(nums, 0, len(nums) - 1)
        return nums

    def _quicksort(self, nums, lo, hi):
        if lo >= hi:
            return
        
        p = self._partition(nums, lo, hi)
        self._quicksort(nums, lo, p - 1)
        self._quicksort(nums, p + 1, hi)

    def _partition(self, nums, lo, hi):
        import random
        rand_idx = random.randint(lo, hi)
        nums[rand_idx], nums[hi] = nums[hi], nums[rand_idx]

        pivot = nums[hi]
        i = lo
        for j in range(lo, hi):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[hi] = nums[hi], nums[i]
        return i