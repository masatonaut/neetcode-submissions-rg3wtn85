class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                return result + intervals[i:]

            elif interval[1] < newInterval[0]:
                result.append(interval)

            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1])
                ]

        result.append(newInterval)
        return result