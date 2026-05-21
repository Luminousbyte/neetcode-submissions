class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        count = 0

        def dfs(r,c):
            nonlocal count
            if (r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]==0):
                count += 1
                return count

            if (r,c) in visit:
                return
            
            visit.add((r,c))

            directions = ((-1,0),(1,0),(0,-1),(0,1))
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r,c)
                    return count
        return 0