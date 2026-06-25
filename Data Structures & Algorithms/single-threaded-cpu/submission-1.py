class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(enq, proc, i) for i, (enq, proc) in enumerate(tasks)])

        heap = []
        result = []
        i = 0
        time = 0
        n = len(tasks)

        while len(result) < n:
            while i < n and tasks[i][0] <= time:
                enq, proc, idx = tasks[i]
                heapq.heappush(heap, (proc, idx))
                i += 1

            if not heap:
                time = tasks[i][0]
                continue

            proc, idx = heapq.heappop(heap)
            result.append(idx)
            time += proc

        return result