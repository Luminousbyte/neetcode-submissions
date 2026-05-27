class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outgoing = defaultdict(int)
        incoming = defaultdict(int)

        for o, i in trust:
            outgoing[i] += 1
            incoming[o] += 1

        for r in range(1, n+1):
            if outgoing[r] == n-1 and incoming[r] == 0:
                return r
        return -1