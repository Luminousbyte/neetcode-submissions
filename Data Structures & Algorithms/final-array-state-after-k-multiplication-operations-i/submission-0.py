class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        lst = []
        for id, val in enumerate(nums):
            lst.append([val, id])
        print(lst)
        while k:
            heapq.heapify(lst)
            x = heapq.heappop(lst)
            k -= 1
            x[0] = x[0] * multiplier
            # x[1] = lst[-1][1] + 1
            heapq.heappush(lst, x)
            print(lst)
        lst.sort(key = lambda x:x[1])
        f_lst = []
        for v, k in lst:
            f_lst.append(v)
        return f_lst