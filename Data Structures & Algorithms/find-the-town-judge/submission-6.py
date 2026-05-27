class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)

        for o, i in trust:
            delta[o] -= 1
            delta[i] += 1

        for r in range(1, n+1):
            if delta[r] == n-1:
                return r
        return -1