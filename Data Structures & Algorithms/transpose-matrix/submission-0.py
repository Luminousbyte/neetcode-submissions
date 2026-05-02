class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        res = []
        for i in range(cols):
            res.append([0]*rows)

        for r in range(rows):
            for c in range(cols):
                res[c][r] = matrix[r][c]

        return res