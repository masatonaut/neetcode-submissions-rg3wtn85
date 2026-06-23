"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def is_same(row, col, size):
            first = grid[row][col]
            for r in range(row, row + size):
                for c in range(col, col + size):
                    if grid[r][c] != first:
                        return False
            return True

        def dfs(row, col, size):
            if is_same(row, col, size):
                return Node(grid[row][col] == 1, True, None, None, None, None)
            half = size // 2
            return Node(
                True, False,
                dfs(row, col, half),
                dfs(row, col + half, half),
                dfs(row + half, col, half),
                dfs(row + half, col + half, half),
            )

        return dfs(0, 0, len(grid))