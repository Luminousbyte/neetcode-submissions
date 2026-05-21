class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        def bfs(r,c):
            q = deque([(r,c)])
            visit.add((r,c))
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            perimeter = 0
            while q:
                x, y = q.popleft()
                for dr, dc in directions:
                    nx, ny = x+dr, y+dc
                    if (nx<0 or ny<0 or nx>=ROWS or ny>=COLS or grid[nx][ny] == 0):
                        perimeter += 1
                    elif (nx, ny) not in visit:
                        visit.add((nx, ny))
                        q.append((nx, ny))
            return perimeter

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return bfs(r,c)
        return 0