class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return len(nums)
            
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
            
        return len(nums)
            