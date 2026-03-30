class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))

        heap = [(0, k)]
        visit = set()

        while heap:
            dist, node = heapq.heappop(heap)
            if node in visit:
                continue

            visit.add(node)

            if len(visit) == n:
                return dist

            for neighbor, time in graph[node]:
                heapq.heappush(heap, [(dist + time), neighbor])

        return -1
