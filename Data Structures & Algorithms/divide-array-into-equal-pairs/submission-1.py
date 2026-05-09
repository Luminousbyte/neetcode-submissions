class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashset = Counter(nums)
        print(hashset)
        for v in hashset.values():
            if v%2 != 0:
                return False
        return True