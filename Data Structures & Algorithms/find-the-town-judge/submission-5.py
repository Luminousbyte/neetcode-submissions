class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outgoing = defaultdict(int)
        incoming = defaultdict(int)

        for o, i in trust:
            outgoing[o] += 1
            incoming[i] += 1

        for r in range(1, n+1):
            if outgoing[r] == 0 and incoming[r] == n-1:
                return r
        return -1