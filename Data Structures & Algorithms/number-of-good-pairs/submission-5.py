class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        pairs = 0
        for v in hashmap.values():
            pairs += (v*(v-1))//2
        return pairs