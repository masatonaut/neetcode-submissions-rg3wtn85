class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        n = len(nums)
        return [num for num, count in counts.items() if count > n // 3]