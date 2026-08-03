class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for n in nums:
            hm[n] += 1
        print(hm)
        lst = []
        for key, v in hm.items():
            lst.append([v,key])
        
        lst.sort()
        print(lst)
        lst1 = []
        while k>0:
            x = lst.pop()
            k -= 1
            lst1.append(x[1])
        return lst1