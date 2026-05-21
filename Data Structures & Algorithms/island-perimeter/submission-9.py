class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        perimeter = 0

        def dfs(r, c):
            nonlocal perimeter
            if (r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == 0):
                perimeter += 1
                return perimeter

            if (r,c) in visit:
                return 0
            
            visit.add((r,c))
            directions = [(0,1), (0,-1), (1,0), (-1, 0)]
            
            for dr, dc in directions:
                dfs(r+dr, c+dc)

            return perimeter

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return dfs(r,c)
        return 0