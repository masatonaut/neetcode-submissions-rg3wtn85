class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visit, prev_height):
            if (r < 0 or r == ROWS or 
                c < 0 or c == COLS or
                (r, c) in visit or
                heights[r][c] < prev_height):
                return
            
            visit.add((r, c))
            
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r + dr, c + dc, visit, heights[r][c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    dfs(r, c, pacific, heights[r][c])
                if r == ROWS - 1 or c == COLS - 1:
                    dfs(r, c, atlantic, heights[r][c])
        
        return [[r, c] for r in range(ROWS) for c in range(COLS)
                if (r, c) in pacific and (r, c) in atlantic]