class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = []
        for x, y in points:
            ec_dist = math.sqrt((x**2) + (y**2))
            lst.append((ec_dist, [x, y]))

        lst1 = []
        heapq.heapify(lst)
        while k>0:
            lst1.append(heapq.heappop(lst)[1])
            k -= 1
        return lst1
