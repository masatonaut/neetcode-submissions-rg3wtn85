import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        heap = [(-cnt, ch) for ch, cnt in count.items()]
        heapq.heapify(heap)

        result = []
        prev = None
        while heap:
            cnt, ch = heapq.heappop(heap)
            result.append(ch)
            cnt += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None
            
            if cnt < 0:
                prev = (cnt, ch)

        result = "".join(result)
        return result if len(result) == len(s) else ""