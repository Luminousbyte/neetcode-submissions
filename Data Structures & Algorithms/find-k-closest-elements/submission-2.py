class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lst = []
        for num in arr:
            lst.append([abs(x-num), num])
        heapq.heapify(lst)
        lst1 = []
        while k:
            lst1.append(heapq.heappop(lst)[1])
            k -= 1
        lst1.sort()
        return lst1