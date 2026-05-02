class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        #conditions:
        #repeating numbers should be captured
        #any missing numbers with range(1-n^2) should be captured

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        lst = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] in visit:
                    lst.append(grid[r][c])
                visit.add(grid[r][c])
        
        for i in range(1, 1+ROWS**2):
            if i not in visit:
                lst.append(i)
        return lst