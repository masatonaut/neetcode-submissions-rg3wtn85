class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n // 2 - 1, -1, -1):
            self._heapify(nums, n, i)

        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            self._heapify(nums, end, 0)

        return nums

    def _heapify(self, nums, size, root):
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < size and nums[left] > nums[largest]:
            largest = left
        if right < size and nums[right] > nums[largest]:
            largest = right

        if largest != root:
            nums[root], nums[largest] = nums[largest], nums[root]
            self._heapify(nums, size, largest)