class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses

        reach = [[False] * n for _ in range(n)]

        for a, b in prerequisites:
            reach[a][b] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if reach[i][k] and reach[k][j]:
                        reach[i][j] = True

        return [reach[u][v] for u, v in queries]