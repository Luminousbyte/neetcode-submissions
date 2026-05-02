class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        self.count = 0

        def dfs(r, c):
            if (r<0 or c<0 or
                r>=ROWS or c>=COLS or
                grid[r][c] == 0):
                self.count += 1
                return self.count

            if (r,c) in visit:
                return

            visit.add((r,c))

            dfs(r+1,c) 
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
            return self.count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return self.count
        return 0