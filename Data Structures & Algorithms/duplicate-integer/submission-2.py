class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in nums[i+1:]:
                if nums[i] == j:
                    return True
        return False