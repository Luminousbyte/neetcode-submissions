class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1

        for values in hashmap.values():
            if values > 1:
                return True
        return False