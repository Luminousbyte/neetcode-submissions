class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        self.perimeter = 0

        def dfs(r,c):

            if (r<0 or c<0 or
                r>=ROWS or c>=COLS
                or grid[r][c] == 0):
                self.perimeter += 1
                return

            if (r,c) in visit:
                return 0

            visit.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and (r,c) not in visit:
                     dfs(r,c)
        return self.perimeter