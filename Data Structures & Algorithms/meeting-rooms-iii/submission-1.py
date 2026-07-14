import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0] * n
        available = list(range(n))
        heapq.heapify(available)
        used = []

        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(used, (end, room))
                count[room] += 1
            else:
                free_time, room = heapq.heappop(used)
                duration = end - start
                heapq.heappush(used, (free_time + duration, room))
                count[room] += 1

        return count.index(max(count))