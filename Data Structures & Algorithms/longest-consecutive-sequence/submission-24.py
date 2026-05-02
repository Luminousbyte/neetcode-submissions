class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        if not nums:
            return 0       
        nums.sort()
        count = 1
        maxcount = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                count = 1
            maxcount = max(maxcount, count)
        return maxcount