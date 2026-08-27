class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1

        lst = []
        for key, v in dic.items():
            lst.append([v,key])
        lst.sort()

        lst1 = []
        while len(lst1)<k:
            lst1.append(lst.pop()[1])

        return lst1