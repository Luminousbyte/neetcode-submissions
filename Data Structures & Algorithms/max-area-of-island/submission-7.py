class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        max_len = 0

        def dfs(r,c):
            length = 0
            if (r<0 or c<0
                or r>=ROWS or c>=COLS
                or not grid[r][c]
                or (r,c) in visit):
                return 0
            
            visit.add((r,c))

            return (1 + 
                    dfs(r+1, c) + 
                    dfs(r-1, c) +
                    dfs(r, c+1) +
                    dfs(r, c-1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    max_len = max(max_len, dfs(r,c))
        return max_len