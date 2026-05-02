class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        streak, max_streak, curr, i = 0, 0, nums[0], 0

        while i < len(nums):
            if nums[i] != curr:
                curr = nums[i]
                streak = 0
            while i<len(nums):
                if nums[i] == curr:
                    i += 1
                else:
                    break
            streak += 1
            curr += 1
            max_streak = max(streak, max_streak)
        return max_streak