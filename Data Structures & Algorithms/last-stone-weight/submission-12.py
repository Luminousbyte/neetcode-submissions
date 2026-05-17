class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-i for i in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)
            if second > first:
                print(f"first:", first)
                print(f"second:", second)
                diff = first - second
                print(f"diff:", diff)
                heapq.heappush(max_heap, diff)
        max_heap.append(0)
        return abs(max_heap[0])
