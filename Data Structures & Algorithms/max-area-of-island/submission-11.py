class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        m_area = 0

        def bfs(r,c):
            q = deque([(r,c)])
            visit.add((r,c))
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            area = 1
            while q:
                nr, nc = q.popleft()
                for dr, dc in directions:
                    rows, cols = nr+dr, nc+dc
                    if (rows<0 or cols<0 or rows>=ROWS or cols>=COLS
                        or not grid[rows][cols] or (rows, cols) in visit):
                        continue
                    q.append((rows, cols))
                    visit.add((rows, cols))
                    area += 1
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and (r,c) not in visit:
                    m_area = max(m_area, bfs(r,c))
        return m_area