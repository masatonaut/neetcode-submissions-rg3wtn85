class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1

        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        result = []

        while q:
            crs = q.popleft()
            result.append(crs)
            for nxt in graph[crs]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return result if len(result) == numCourses else []