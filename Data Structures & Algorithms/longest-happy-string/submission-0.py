import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for cnt, ch in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if cnt != 0:
                heapq.heappush(heap, (cnt, ch))

        result = []

        while heap:
            cnt, ch = heapq.heappop(heap)

            if len(result) >= 2 and result[-1] == result[-2] == ch:
                if not heap:
                    break
                cnt2, ch2 = heapq.heappop(heap)
                result.append(ch2)
                cnt2 += 1
                if cnt2 < 0:
                    heapq.heappush(heap, (cnt2, ch2))
                heapq.heappush(heap, (cnt, ch))
            else:
                result.append(ch)
                cnt += 1
                if cnt < 0:
                    heapq.heappush(heap, (cnt, ch))

        return "".join(result)