class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)
        for n in nums:
            if n in nums_dict:
                nums_dict[n] += 1
            else:
                nums_dict[n] = 1

        lst = []
        for key, val in nums_dict.items():
            lst.append([val, key])
        lst.sort()

        lst1 = []
        while k > 0:
            x = lst.pop()[1]
            lst1.append(x)
            k -= 1
        
        return lst1