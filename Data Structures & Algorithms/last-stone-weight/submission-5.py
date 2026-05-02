from _heapq import heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_maxq = [-i for i in stones]
        heapq.heapify(stones_maxq)
        
        while len(stones_maxq)>1:
            
            sub = -(heapq.heappop(stones_maxq)) + heapq.heappop(stones_maxq)
            heapq.heappush(stones_maxq, -sub)

        return abs(stones_maxq[0])