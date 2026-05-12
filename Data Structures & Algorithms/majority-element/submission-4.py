class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        
        return max(hashmap, key = hashmap.get)