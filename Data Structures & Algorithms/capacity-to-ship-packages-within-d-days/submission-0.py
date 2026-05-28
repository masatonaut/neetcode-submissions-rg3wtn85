class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        def days_needed(capacity):
            d = 1
            current = 0
            for w in weights:
                if current + w > capacity:
                    d += 1
                    current = w
                else:
                    current += w
            return d

        while left < right:
            mid = (left + right) // 2

            if days_needed(mid) <= days:
                right = mid
            else:
                left = mid + 1

        return left