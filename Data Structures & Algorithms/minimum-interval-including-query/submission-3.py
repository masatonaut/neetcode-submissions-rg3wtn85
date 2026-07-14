class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        answer = {}
        heap = []
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                heapq.heappush(heap, (right - left + 1, right))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            answer[q] = heap[0][0] if heap else -1

        return [answer[q] for q in queries]
