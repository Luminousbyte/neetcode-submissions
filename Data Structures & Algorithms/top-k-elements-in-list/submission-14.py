class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        alm = defaultdict(int)
        for i in nums:
            alm[i] += 1

        lst = []
        for keys, values in alm.items():
            lst.append([values, keys])

        lst.sort()
        print(lst)
        lst1 = []
        while k>0:
            y = lst.pop()
            lst1.append(y[1])
            k -= 1
        return lst1