class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for contents in nums:
            if contents in hashmap:
                hashmap[contents] += 1
            else:
                hashmap[contents] = 1

        for value in hashmap.values():
            if value > 1:
                return True
        return False
