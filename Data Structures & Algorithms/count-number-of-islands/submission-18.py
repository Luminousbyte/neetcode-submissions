class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        count = 0

        def bfs(r,c):
            q = deque([[r,c]])
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            visit.add((r,c))
            while q:
                nr, nc = q.popleft()
                for dr, dc in directions:
                    ir, ic = (nr + dr), (nc + dc)
                    if (ir >= 0 and ic >= 0 
                        and ir < ROWS and ic < COLS 
                        and grid[ir][ic] == "1" 
                        and (ir, ic) not in visit):
                        q.append([nr + dr, nc + dc])
                        visit.add((nr+dr, nc+dc))
                    

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    count += 1
        return count