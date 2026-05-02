class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for contents in nums:
            hashmap[contents] = hashmap.get(contents, 0) + 1

        for value in hashmap.values():
            if value > 1:
                return True
        return False
