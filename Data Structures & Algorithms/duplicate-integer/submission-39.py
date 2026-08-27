class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_n = set(nums)
        return len(nums) != len(set_n)