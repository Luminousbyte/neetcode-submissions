class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        
        lst = []
        for key, v in hashmap.items():
            lst.append([v, key])
        
        lst.sort()
        lst2 = []
        while k:
            x = lst.pop()
            k -= 1
            lst2.append(x[1])

        return lst2