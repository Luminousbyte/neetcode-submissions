class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        streak, curr, res, i = 0, nums[0], 0, 0

        while i<len(nums):
            if nums[i] != curr:
                curr = nums[i]
                streak = 0
            while i<len(nums) and nums[i] == curr:
                i += 1
            curr += 1
            streak += 1
            res = max(streak, res)
        return res