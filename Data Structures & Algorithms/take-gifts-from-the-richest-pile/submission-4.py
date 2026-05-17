class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_gifts = [-i for i in gifts]
        heapq.heapify(max_gifts)
        # print(max_gifts)
        while k:
            x = heapq.heappop(max_gifts)
            # print(x)
            floor_val = (-int(abs(x)**0.5))
            # print(max_gifts)
            k -= 1
            heapq.heappush(max_gifts, floor_val)
        return abs(sum(max_gifts))