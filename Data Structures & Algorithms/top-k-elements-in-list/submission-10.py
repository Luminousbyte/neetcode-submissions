class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        lst = []
        for item, times in count.items():
            lst.append([times, item])
        lst.sort()
        
        result = []
        while len(result)<k:
            result.append(lst.pop()[1])
        
        return result