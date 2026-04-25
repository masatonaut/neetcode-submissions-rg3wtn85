class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])

        keep = 1
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if prev_end <= intervals[i][0]:
                keep += 1
                prev_end = intervals[i][1]

        return len(intervals) - keep