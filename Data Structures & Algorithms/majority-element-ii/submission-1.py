class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = 0, 1
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        n = len(nums)
        for c in (candidate1, candidate2):
            if nums.count(c) > n // 3:
                result.append(c)

        return result